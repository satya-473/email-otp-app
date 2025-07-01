import streamlit as st
import smtplib
import random
import time
import os
import re
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from .env file
load_dotenv()
EMAIL = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASS")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

COOLDOWN_SECONDS = 60  # Time before resend allowed

# Initialize session state
if "otp" not in st.session_state:
    st.session_state.otp = None
if "otp_time" not in st.session_state:
    st.session_state.otp_time = None
if "email_sent" not in st.session_state:
    st.session_state.email_sent = False
if "last_sent_time" not in st.session_state:
    st.session_state.last_sent_time = 0
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# Validate email format
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Send OTP via email
def send_otp(email):
    otp = random.randint(1000, 9999)
    body = f"Your OTP for verification is: {otp}"

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = email
    msg["Subject"] = "OTP for Verification"
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        st.success(f"✅ OTP sent successfully to {email}")
        return otp
    except Exception as e:
        st.error(f"❌ Failed to send OTP: {e}")
        return None
    finally:
        server.quit()

# Cooldown logic
def get_cooldown_remaining():
    elapsed = time.time() - st.session_state.last_sent_time
    return max(0, COOLDOWN_SECONDS - int(elapsed))

# UI
st.title("🔐 Email OTP Verification")

email_input = st.text_input("📧 Enter your email:", value=st.session_state.user_email)

cooldown_remaining = get_cooldown_remaining()

if st.button("Send OTP", disabled=cooldown_remaining > 0):
    if not EMAIL or not PASSWORD:
        st.error("⚠️ Email server credentials are missing in .env.")
    elif not is_valid_email(email_input):
        st.warning("⚠️ Please enter a valid email address.")
    else:
        otp = send_otp(email_input)
        if otp:
            st.session_state.otp = otp
            st.session_state.otp_time = time.time()
            st.session_state.last_sent_time = time.time()
            st.session_state.email_sent = True
            st.session_state.user_email = email_input
            st.rerun()  # 🔁 Refresh UI to show OTP field immediately

if st.session_state.email_sent:
    st.info(f"📩 OTP sent to {st.session_state.user_email}. Resend allowed in: {get_cooldown_remaining()} seconds")

    entered_otp = st.text_input("🔢 Enter the OTP you received:")

    if st.button("Verify OTP"):
        if not entered_otp.isdigit() or len(entered_otp) != 4:
            st.warning("⚠️ Please enter a valid 4-digit OTP.")
        elif time.time() - st.session_state.otp_time > 300:
            st.error("⏳ OTP expired. Please request a new one.")
            st.session_state.email_sent = False
            st.session_state.otp = None
        elif int(entered_otp) == st.session_state.otp:
            st.success("🎉 OTP verified successfully!")
            st.session_state.email_sent = False
            st.session_state.otp = None
        else:
            st.error("❌ Invalid OTP. Please try again.")
