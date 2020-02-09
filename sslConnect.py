
#%%

#%%
import smtplib
import os 
import imghdr

from email.message import EmailMessage 
EMAIL_ADDRESS =os.environ.get('myGmailAddress')
EMAIL_PASSWORD = os.environ.get("googleAppPasswordPython")
msg  = EmailMessage()
msg['Subject'] = "Testing for the third"
msg["From"]  =  EMAIL_ADDRESS
msg['To'] = 'ale.macca@hotmail.com'
msg.set_content("i love you  ")


 
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



