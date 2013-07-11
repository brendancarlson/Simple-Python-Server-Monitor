#!/usr/bin/python

import smtplib
import os
import time
import datetime
from configuration import settings

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

"""Sends an e-mail to the specified recipient."""
sender = settings["monitor_email"]
recipient = settings["recipient_email"]
subject = settings["email_subject"]
headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)
session = smtplib.SMTP(settings["monitor_server"], settings["monitor_server_port"])
session.ehlo()
session.starttls()
session.login(settings["monitor_email"], settings["monitor_password"])
response = os.system("ping -c 1 " + settings["hostname"])

# If the site is up, do noting
if response == 0: 
    session.quit()
else:
    # If the site is down, send the email
    body = settings["hostname"] + " " + "is down at" + " " + st
    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()