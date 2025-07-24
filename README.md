

This project is a simple, automated email sender built with Python. It uses Gmail's SMTP server to send scheduled emails daily at a specified time using the smtplib and schedule libraries.

---

## 🔧 Features

- Sends automatic emails using your Gmail account
- Customizable subject and body
- Schedule to send daily at a specific time
- Simple and lightweight
- Can run in the background continuously

---

## 🛠 Requirements

- Python 3.x
- Gmail account with App Password enabled
- Packages:
  - schedule (install via pip install schedule)

---

## 🔐 Gmail Setup

To use this script with Gmail:

1. *Enable 2-Step Verification* on your Google Account:  
   [https://myaccount.google.com/security](https://myaccount.google.com/security)

2. *Generate an App Password*:  
   Go to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)  
   Select "Mail" and "Windows Computer", then copy the 16-character password.

3. Use this password in the script instead of your actual Gmail password.

---

## 🧪 How to Run

1. Clone or download this repository.
2. Open auto_email_sender.py (or your Python file).
3. Replace these variables with your real info:

   ```python
   sender_email = "your_email@gmail.com"
   sender_password = "your_app_password"
   receiver_email = "recipient@example.com"
