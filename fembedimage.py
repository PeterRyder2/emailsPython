import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
#from email.MIMEImage import MIMEImage
EMAIL_ADDRESS = os.environ.get('myGmailAddress')
EMAIL_PASSWORD = os.environ.get("googleAppPasswordPython")
msg = MIMEMultipart('related')
msg['Subject'] = "Test"
msg['From'] = "peter.ryder2@gmail.com"
msg['To'] = "peter.ryder2@gmail.com"

html = """\
<html>
  <head></head>
    <body>
      <img src="cid:image1" alt="Logo" style="width:250px;height:50px;"><br>
       <p><h4 style="font-size:15px;">Some Text.</h4></p>           
    </body>
</html>
"""
# Record the MIME types of text/html.
part2 = MIMEText(html, 'html')

# Attach parts into message container.
msg.attach(part2)

# This example assumes the image is in the current directory
fp = open('MUNSTER.JPEG', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

# Send the message via local SMTP server.
# mailsrv = smtplib.SMTP('localhost')
# mailsrv.sendmail("peter.ryder2@gmail.com", "peter.ryder2@gmail.com", msg.as_string())
# mailsrv.quit()

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    #from email.MIMEImage import MIMEImage
    EMAIL_ADDRESS = os.environ.get('myGmailAddress')
    EMAIL_PASSWORD = os.environ.get("googleAppPasswordPython")
    msg = MIMEMultipart('related')
    msg['Subject'] = "Test"
    msg['From'] = "peter.ryder2@gmail.com"
    msg['To'] = "peter.ryder2@gmail.com"

    html = """\
    <html>
    <head></head>
        <body>
        <img src="cid:image1" alt="Logo" style="width:250px;height:50px;"><br>
        <p><h4 style="font-size:15px;">Some Text.</h4></p>           
        </body>
    </html>
    """
    # Record the MIME types of text/html.
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part2)

    # This example assumes the image is in the current directory
    fp = open('MUNSTER.JPEG', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)


    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "Grabb Dinner this evening"#
    body = "Dinner later"

    msg = f"Subject: {subject}\n\n {body}"

    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.)