Simple-Python-Server-Monitor
============================

Super simple Python based server ping monitor. Emails you with a gmail address if server is down.

============================

1. Add the IP address or hostname of the server you would like to monitor.
  hostname = '8.8.8.8'  #your servers hostname or IP address
2.Add the hostname or ip address and the recipient email 
  recipient_email = 'recipient@yourdomain.com' #receiving email address (to)  
3. Add the gmail address you would like to send the email from when your server goes down and the password.
  monitor_email = 'monitor@yourdomain.com' #monitor email address (from)
  monitor_pwd = 'monitor email password' #monitor email password
4. Add script to crontab to run every x amount of minutes you would like to run it.


