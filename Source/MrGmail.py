# -*- coding: UTF-8 -*-
import email, imaplib, os, time, sys

<<<<<<< HEAD

def DetachEmails(user, pwd, workingDirectory, condition=[]):
=======
def DetachEmails (user, pwd, workingDirectory, condition=[]):

>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
    # connecting to the gmail imap server
    try:
        m = imaplib.IMAP4_SSL("imap.gmail.com")
        m.login(user, pwd)
        m.select("Inbox")  # here you a can choose a mail box like INBOX instead
        # use m.list() to get all the mailboxes

        ##    m.literal = u"לאומי".encode('utf-8')
        ##    m.uid('SEARCH', 'CHARSET', 'UTF-8', 'SUBJECT')
        resp, items = m.search(None, "FROM", "secure.mail@bankleumi.co.il")
        # resp, items = m.search(None, "SENTBEFORE", "1-Jan-2018", "FROM", "secure.mail@bankleumi.co.il")
<<<<<<< HEAD
        ## "ALL")  # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
    except Exception as e:
        print >> sys.stderr, '*** IMAP exception: %s' % (e)
        m.logout()
        return (False)
=======
            ## "ALL")  # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
    except:
        m.logout()
        return(1)

>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
    items = items[0].split()  # getting the mails id

    for emailid in items:
        resp, data = m.fetch(emailid,
<<<<<<< HEAD
                             "(RFC822)")  # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
=======
                         "(RFC822)")  # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
        email_body = data[0][1]  # getting the mail content
        mail = email.message_from_string(email_body)  # parsing the mail content to get a mail object

        # Check if any attachments at all
        if mail.get_content_maintype() != 'multipart':
            continue

        try:
<<<<<<< HEAD
            tn = time.strptime(mail["Date"][0:24],
                               "%a, %d %b %Y %H:%M:%S")  ## Ignore TZ offset as there is a bug in strptime
=======
            tn = time.strptime(mail["Date"][0:24], "%a, %d %b %Y %H:%M:%S") ## Ignore TZ offset as there is a bug in strptime
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
        except Exception as e:
            print >> sys.stderr, 'Time stamp of mail id %s doesn"t match\n %s' % (emailid, e)
            break
        date_filename = "%04d%02d%02d" % (tn.tm_year, tn.tm_mon, tn.tm_mday)
        # print "[" + mail["Date"] + "] :" + mail["Return-Path"] + date_filename

        # we use walk to create a generator so we can iterate on the parts and forget about the recursive headach
        for part in mail.walk():
            # multipart are just containers, so we skip them
            if part.get_content_maintype() == 'multipart':
                continue

            # is this part an attachment ?
            if part.get('Content-Disposition') is None:
                continue

            # filename = part.get_filename()
            for i in range(1, 19):
<<<<<<< HEAD
                filename = date_filename + " " + str(i) + ".PDF"
                att_path = os.path.join(workingDirectory, filename)

                # Check if its already there
                if os.path.isfile(att_path):
                    continue
                else:  # finally write the stuff
                    fp = open(att_path, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                    resp = m.store(emailid, '+FLAGS', '\\Deleted')  # archive the message
=======
                filename = date_filename + " " + str(i) +".PDF"
                att_path = os.path.join(workingDirectory, filename)

            # Check if its already there
                if os.path.isfile(att_path):
                    continue
                else:    # finally write the stuff
                    fp = open(att_path, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
                    resp = m.store(emailid, '+FLAGS', '\\Deleted') # archive the message
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
                    if resp[0] != 'OK':
                        print >> sys.stderr, 'Could not archive message %s' % tn
                    break

    m.logout()
<<<<<<< HEAD
    return (True)
=======
    return(0)
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
