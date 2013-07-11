Simple Python Server Monitor
============================

Super simple Python based server ping monitor. Emails you with any email address (default: Gmail) if server is down.

Configuration for Gmail (Easiest)
---------------------------------

Open the configuration.py file with your favorite text editor.

1. Add the IP address or hostname of the server you would like to monitor.

        "hostname": '8.8.8.8', # Put your server in place of the 8.8.8.8 (Keep the quotation marks)

2. Add the hostname or ip address and the recipient email

        "recipient_email": 'recipient@yourdomain.com', # The email that the alerts will be sent to


3. Add the Gmail address you would like to send the email from when your server goes down.

        "monitor_email": 'your_gmail_username@gmail.com',

4. Add the Gmail password that is associated with the above Gmail email address

        "monitor_password": 'gmail password',

5. Add script to crontab to run every x amount of minutes you would like to run it.


Configuration for a custom email account
----------------------------------------

Open the configuration.py file with your favorite text editor.

1. Add the IP address or hostname of the server you would like to monitor.

        "hostname": '8.8.8.8', # Put your server in place of the 8.8.8.8 (Keep the quotation marks)

2. Add the hostname or ip address and the recipient email

        "recipient_email": 'recipient@yourdomain.com', # The email that the alerts will be sent to


3. Add the email address you would like to send the email from when your server goes down.

        "monitor_email": 'your_gmail_username@yourdomain.com',

4. Add the email password that is associated with the above email address

        "monitor_password": 'email password',

5. Set the email server (smtp) address to send the emails from

        "monitor_server": 'smtp.yourdomain.com',

6. Set the email server port

        "monitor_server_port": 587,

5. Add script to crontab to run every x amount of minutes you would like to run it.


Optional Settings
-----------------

You can optionally set the subject of the email that is sent when the server goes down

    "email_subject": 'Subject of the email'

