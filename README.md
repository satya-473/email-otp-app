# 🔐 Email OTP Verification App

This is a simple Streamlit web app to verify users via OTP (One-Time Password) sent to their email address.

## 🚀 Features

- User enters their email address
- OTP is sent securely via Gmail SMTP
- 4-digit OTP randomly generated
- Resend cooldown timer (60 seconds)
- OTP expires after 5 minutes
- Validates email format and OTP

## 🌐 Live Demo

👉 [Click here to try the app](https://email-otp-app-46oupmr4jbbutgyak4fbxp.streamlit.app)

## 🔧 Technologies Used

- Python
- Streamlit
- smtplib
- dotenv
- Email MIME (smtplib)

## 📁 Folder Structure
email-otp-app/
│
├── main.py
├── requirements.txt
├── .env (not uploaded to GitHub)
└── README.md

## ⚙️ Setup Instructions (For Local Use)

1. **Clone the repository**

```bash
git clone https://github.com/satya-473/email-otp-app.git
cd email-otp-app


2. **Install the required packages**

```bash
pip install -r requirements.txt
```

3. **Setup `.env` file**

Create a `.env` file in the root directory and add:

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password_or_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

⚠️ **If using Gmail**, make sure to enable [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) and use that instead of your regular password.

🚀 **Deploy on Streamlit Cloud**

-- > Push the project to GitHub.
-- > Go to streamlit.io → "Create app".
-- > Connect your GitHub repo.
--> Add secrets via the ☰ → Settings → Secrets option like this:

EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password_or_app_password  
SMTP_SERVER=smtp.gmail.com  
SMTP_PORT=587

 4. **Run the app**
 streamlit run main.py

 5. **🙋‍♂️ Author**
Made with ❤️ by Satya
GitHub: satya-473

---

Let me know once you've updated it — I can help you make it even better if you'd like!


 
















  


