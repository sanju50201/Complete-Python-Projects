import time
import requests
import smtplib
from email.mime.text import MIMEText


class UptimeBot:
    def __init__(self, alert_threshold=3600, email_alert=None):
        self.start_time = time.time()
        self.alert_threshold = alert_threshold  # 1 hour in seconds
        self.alert_sent = False
        self.email_alert = email_alert


    def get_uptime(self):
        current_time = time.time()
        uptime = current_time - self.start_time
        return int(uptime)

    def send_alert(self):
        # Send an alert via email
        if self.email_alert:
            subject = "Uptime Alert"
            body = f"Uptime has exceeded {self.alert_threshold} seconds"
            message = MIMEText(body)
            message['Subject'] = subject
            message['From'] = 'sender@example.com'
            message['To'] = self.email_alert
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login('sender@example.com', 'password')
                smtp.send_message(message)
                print("Alert sent successfully via email")
        else:
            print("Alert: Uptime threshold exceeded!")

    def check_alert(self):
        uptime = self.get_uptime()
        if uptime > self.alert_threshold and not self.alert_sent:
            self.send_alert()
            self.alert_sent = True

    def reset_alert(self):
        self.alert_sent = False

    def change_alert_threshold(self, new_threshold):
        self.alert_threshold = new_threshold
        self.reset_alert()

    def run(self):
        while True:
            uptime = self.get_uptime()
            print(f"Uptime: {uptime} seconds")
            self.check_alert()
            time.sleep(60)  # Sleep for 60 seconds


bot = UptimeBot(alert_threshold=7200, email_alert="recipient@example.com")
bot.run()
