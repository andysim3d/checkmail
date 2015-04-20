#! /usr/bin/python
import imaplib
import os
import mail 

path = "/Users/Andy/Documents/myscripts/checkmail/"

from pync import Notifier 

M = imaplib.IMAP4_SSL("imap.gmail.com", 993)



M.login(mail.mailbox,mail.password) 
status, count = M.status("Inbox", "(MESSAGES UNSEEN)")
unread = count[0].split()[4][:-1]
if int(unread) == 0:
	Notifier.notify("No unread mails.", title= mail.mailbox ,appIcon="%sicon.ico"%path)
else:
	Notifier.notify("You have %s mail(s) unread."%str(unread), title=mail.mailbox , appIcon="%sicon.ico"%path ,sound="Ping")

M.logout()

