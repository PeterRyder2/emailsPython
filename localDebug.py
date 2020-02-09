#%%
#####
# Important: run  python -m smtpd -c DebuggingServer -n localhost:1025
# for debug server to work


# Sends a debug email on a debug server if you dont want 
# to send messges to each other
#####

import smtplib
import os 
EMAIL_ADDRESS = 'peter.ryder2@gmail.com'
EMAIL_PASSWORD = os.environ.get("googleAppPasswordPython")
with smtplib.SMTP('localhost', 1025) as smtp:

    subject = "Grabb Dinner this evening"#
    body = "Dinner later"

    msg = f"Subject: {subject}\n\n {body}"

    smtp.sendmail(EMAIL_ADDRESS, 'peter.ryder2@gmail.com', msg)





# %%
