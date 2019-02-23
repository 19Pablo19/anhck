import smtplib

sender = 'sp.schoolprotectors@gmail.com'
receivers = ['sp.schoolprotectors@gmail.com']

message = """From: From Person sp.schoolprotectors@gmail.com
To: To Person sp.schoolprotectors@gmail.com
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('aspmx.l.google.com:25')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except :
   print("Error: unable to send email")
