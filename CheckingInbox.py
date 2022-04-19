# import imaplib
# internet message access protocol

import imapclient, pyzmail

# using above third party modules instead

conn = impaclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('youremail', 'yourpass')


# conn.list_folders() will show you list of all folders in tuples for your email
conn.select_folder('INBOX', readonly=True)

# to find emails, list of strings of search keywords can be passed to find emails with a specific search criteria


# lots of different search keys can be used
UIDs = conn.search(['SINCE 20-Aug-2015'])
print(UIDs)


# first passing UID of an email ; then passing some more criteria
rawMessage = conn.fetch([47474], ['BODY[]', 'FLAGS'])



# then use pyzmail to parse through what above returns

message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
# returns pyz message object

message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')


# you can send text emails or html emails (colorful text, images etc)

message.text_part
message.html_part

# you can check if respective html and text parts of email exist or just one or the other

message.text_part.get_payload().decode('UTF-8')

# finally gives you a plain and ordinary string; if doesn't work figure out email's encoding using below

message.text_part.charset
message.text_part.charset == None



# to delete emails
conn.select_folder('INBOX', readonly=False)

UIDs = conn.search(['ON 24-Aug-2015'])
print(UIDs)

# conn.delete_messages(UIDs)




