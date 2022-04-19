# import smtplib

    # simple mail transfer protocol

# conn = smtplib.SMTP('smtp.gmail.com', 587)

    # connection object using smtplib ; 1st argument domain smtp name ; 2nd port typically used for connection

# conn.ehlo()

    # above to establish / starts the connection

# conn.starttls()

    # starts encryption ; need to do this before passing login details

# conn.login('asweigart@gmail.com', 'lxkjfvcrlxxiinmj')

# conn.sendmail('asweigart@gmail.com', 'asweigart@gmail.com', 'Subject: So long...\n\nDear Al,\nSo long, and thanks for all the fish.\n\n-Al')

# conn.quit()

