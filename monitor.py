#!/usr/bin/env python

import smtplib
import os
import time
import datetime
from configuration import settings


class UptimeLogger(object):
    """
    Creates a file to check the last status of the hostname. Works by creating a file when the site is down
    and removing it when it is up
    """
    def __init__(self):
        # Set the file name
        self.file_location = os.path.join(os.getcwd(), 'is_down')

    def was_up(self):
        """
        Checks if the site was up last time. Returns a boolean
        """
        return os.path.exists(self.file_location)

    def mark_down(self):
        """
        Mark the site as down
        """
        open(self.file_location).close()

    def mark_up(self):
        """
        Mark the site as up
        """
        os.remove(self.file_location)

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

uptime_logger = UptimeLogger()

if response == 0:
    # If the site is up, check if the site was previously down
    if not uptime_logger.was_up():
        # The site went from down to up
        body = "%s went back up at %s" % (settings["hostname"], st)
        session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)

else:
    # If the site was not previously down, send the email
    if uptime_logger.was_up():
        body = "%s went down at %s" % (settings["hostname"], st)
        session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)

session.quit()
