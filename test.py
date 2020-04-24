# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
import smtplib
# Define these once; use them twice!
strFrom = 'peter.ryder2@gmail.com'
strTo = 'peter.ryder2@gmail.com'

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('chart.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
# import smtplib
# smtp = smtplib.SMTP()
# smtp.connect('smtp.gmail.com', 587)
EMAIL_ADDRESS = os.environ.get('myGmailAddress')
EMAIL_PASSWORD = os.environ.get("googleAppPasswordPython")
# smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
# smtp.sendmail(strFrom, strTo, msgRoot.as_string())
# smtp.quit()

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "Grabb Dinner this evening"#
    body = "Dinner later"

    msg = f"Subject: {subject}\n\n {body}"
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    #smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)