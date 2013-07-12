Simple Python Server Monitor
============================

Super simple Python based server ping monitor. Emails you with any email address (default: Gmail) if server is down.

Adding Sites
------------

You can add multiple sites to check every minute with the monitor.

1. Open up the configuration.py file

2. Add your site's to the list there. For example, the configuration for checking google and github would be:

        sites = (
            'google.com',
            'github.com',
        )

    **Note:** Each site must have a comma after it


Configuration for Gmail (Easiest)
---------------------------------

Open the configuration.py file with your favorite text editor.

1. Add the hostname or ip address and the recipient email

        "recipient_email": 'recipient@yourdomain.com', # The email that the alerts will be sent to


2. Add the Gmail address you would like to send the email from when your server goes down.

        "monitor_email": 'your_gmail_username@gmail.com',

3. Add the Gmail password that is associated with the above Gmail email address

        "monitor_password": 'gmail password',

4. Add script to crontab to run every x amount of minutes you would like to run it.


Configuration for a custom email account
----------------------------------------

Open the configuration.py file with your favorite text editor.

1. Add the hostname or ip address and the recipient email

        "recipient_email": 'recipient@yourdomain.com', # The email that the alerts will be sent to


2. Add the email address you would like to send the email from when your server goes down.

        "monitor_email": 'your_gmail_username@yourdomain.com',

3. Add the email password that is associated with the above email address

        "monitor_password": 'email password',

4. Set the email server (smtp) address to send the emails from

        "monitor_server": 'smtp.yourdomain.com',

5. Set the email server port

        "monitor_server_port": 587,

6. Add script to crontab to run every x amount of minutes you would like to run it.


Optional Settings
-----------------

You can optionally set the subject of the email that is sent when the server goes down

    "email_subject": 'Subject of the email'

