import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import schedule
import time

# Configuration
sender_email = "youremail@gmail.com"
sender_password = "your_app_password"  # Use App Password if using Gmail
receiver_email = "receiver@example.com"

# Create the email content
def send_email():
    subject = f"Daily Update - {datetime.date.today().strftime('%d %b %Y')}"
    body = "Hello,\n\nThis is your daily automated update.\n\nHave a great day!"

    # Build the message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        # Gmail SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Schedule to run every day at 12:59 AM
schedule.every().day.at("01:00").do(send_email)

print("📧 Email scheduler started. Waiting to send...")

while True:
    schedule.run_pending()
    time.sleep(60)  # check every 1 minutep
