
#%%

#%%
import smtplib
import os 
import imghdr

from email.message import EmailMessage 
EMAIL_ADDRESS = os.environ.get('myGmailAddress')
EMAIL_PASSWORD = os.environ.get("googleAppPasswordPython")
msg  = EmailMessage()
msg['Subject'] = "PDF Test"
msg["From"]  =  EMAIL_ADDRESS
msg['To'] = os.environ.get('myGmailAddress')
msg.set_content("Test File ")

#####
# for images
#####
# picList = ["MUNSTER.jpeg"]
# for files in picList:
#     print(files)
#     with open(files, 'rb' ) as f:
#         fileData = f.read()
#         fileType = imghdr.what(f.name)
#         fileName = f.name
#     msg.add_attachment(fileData, maintype= 'image', subtype =fileType, filename = fileName)


#####
# for PDFs
#####
pdfList = ["test.pdf"]
for files in pdfList:
    print(files)
    with open(files, 'rb' ) as f:
        fileData = f.read()
        fileName = f.name
    msg.add_attachment(fileData, maintype= 'application', subtype ='octet-stream', filename = fileName)



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



# %%
