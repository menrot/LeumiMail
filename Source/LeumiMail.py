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

# Erase all files in a directory
def EraseFiles(mydir):
    files = [f for f in os.listdir(mydir) if os.path.isfile(os.path.join(mydir, f))]
    for f in files:
        os.remove(os.path.join(mydir, f))
    return




### Usage LeumiMail Gmail-username Gmail-password PDF-passport
if len(sys.argv) > 1:
    Guser = sys.argv[1]
else:
    raw_input("Enter your GMail username:")

if len(sys.argv) > 2:
    Gpwd = sys.argv[2]
else:
    Gpwd = getpass.getpass("Enter your GMail password: ")

if len(sys.argv) > 3:
    Dpwd = sys.argv[3]
else:
    Dpwd = getpass.getpass("Enter your Doc password: ")

workingDir = '..\\temp'  # directory where to save attachments (default: current)
emailsDir = workingDir + "\\emails"
attachmentsDir = workingDir + "\\attachments"
accountsFile = "ListOfAccounts.csv"
## Remove all files in the working environment
EraseFiles(emailsDir)
EraseFiles(attachmentsDir)

# Create the accounts table
Accounts = Table()
csv_fp = open('ListOfAccounts.csv', 'rb')
Accounts.populate_Table(csv_fp)

# login to gmail account and for a selected emails, extract the attachments

DetachEmails (Guser, Gpwd, workingDir + "\\emails", condition=[])

# each email attachment which is a PDF file, has its own attachment, usually HTML.
# extract those
files = [f for f in os.listdir(emailsDir)]
for f in files:
    extractembedded(f, password=Dpwd, extractdir = attachmentsDir, emailsDir=emailsDir)

# for each HTML - parse the file, identify the account and date, and rename the file accordingly

ProcessHTML(Accounts, attachmentsDir)




# Open each file, and if approved - move to target folder based on account name

