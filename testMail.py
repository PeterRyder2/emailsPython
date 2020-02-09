
#%%
import smtplib
import os 
EMAIL_ADDRESS = os.environ.get('myGmailAddress')
EMAIL_PASSWORD = os.environ.get("googleAppPasswordPython")
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "Grabb Dinner this evening"#
    body = "Dinner later"

    msg = f"Subject: {subject}\n\n {body}"

    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)




# %%
