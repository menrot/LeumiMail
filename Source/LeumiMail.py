# -*- coding: utf-8 -*-

###
### Read emails from leumi
### Extract attachments
### parse and create files to save
###

import sys, os
import getpass
from MrUtils import Table
from MrGmail import DetachEmails
from MrPDFextract import extractembedded
from ProcessHTML import ProcessHTML
import argparse


# Erase all files in a directory
def EraseFiles(mydir):
    files = [f for f in os.listdir(mydir) if os.path.isfile(os.path.join(mydir, f))]
    for f in files:
        os.remove(os.path.join(mydir, f))
    return

### Usage LeumiMail Gmail-username Gmail-password PDF-passport [NoEmail]
parser = argparse.ArgumentParser(description='Process Leumi email from Gmail')
parser.add_argument('gmailAccount', metavar='gmailAccount', type=str,
                    help='the gmail account having the Leumi email in its Inbox')
parser.add_argument('-p', dest='Gpwd', action='store',
                    help='gmail account password')
parser.add_argument('-P', dest='Dpwd', action='store',
                    help='PDF files password')
parser.add_argument('-Nemail', dest='EmailProcess', action='store_false',   #By default - process email
                    help='When set-gmail is not accessed and recent files are used')

MyArgs = vars(parser.parse_args())

#create variables
locals().update(MyArgs)

#Interactive
if Gpwd == None:
    Gpwd = getpass.getpass("Enter your gmail password: ")
if Dpwd == None:
    Dpwd = getpass.getpass("Enter your Doc password: ")


workingDir = '..\\temp'  # directory where to save attachments (default: current)
emailsDir = workingDir + "\\emails"
attachmentsDir = workingDir + "\\attachments"
accountsFile = "ListOfAccounts.csv"

# Create the accounts table
Accounts = Table()
csv_fp = open('ListOfAccounts.csv', 'rb')
Accounts.populate_Table(csv_fp)

print >>sys.stderr, 'parameters parsed %s, %s, %s, %r' % (gmailAccount, Gpwd[-3:], Dpwd[-4:], EmailProcess)
# login to gmail account and for a selected emails, extract the attachments

## Remove all files in the working environment
if EmailProcess:
    EraseFiles(emailsDir)

    DetachEmails (gmailAccount, Gpwd, workingDir + "\\emails", condition=[])

print >>sys.stderr, 'email logout'
# each email attachment which is a PDF file, has its own attachment, usually HTML.
# extract those
EraseFiles(attachmentsDir)
files = [f for f in os.listdir(emailsDir)]
for f in files:
    extractembedded(f, password=Dpwd, extractdir = attachmentsDir, emailsDir=emailsDir)

print >>sys.stderr, 'attachment extracted'
# for each HTML - parse the file, identify the account and date, and rename the file accordingly

ProcessHTML(Accounts, attachmentsDir)

print "end processing - check temp\\attachments sub direcories"




# Open each file, and if approved - move to target folder based on account name

