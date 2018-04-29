# -*- coding: utf-8 -*-

"""
LeumiMail

    Release V4.0
    This module is to parse and organize notices from Leumi

    There are two main operation modes:
    1. Receiving an encrypted email. This mode was decapitated on March 2018
    2. Downloading the internal Leumi inbox. It creates zip file with HTML members

    The program receives the following parameters

    -Z [location]   where the zip file exists

    The folder environment is as follows:
        script
        temp
            zips
            downloaded
                account_1
                account_2
        emails
        attachments

    In the script folder there has to be a CSV file describing the accounts

    the emails and attachments folders are not used anymore


"""

###
### Read emails from leumi
### Extract attachments
### parse and create files to save
###

import sys, os, shutil
import getpass
from MrUtils import Table
from MrGmail import DetachEmails
from MrPDFextract import extractembedded
from ProcessHTML import ProcessHTML
from MrZip import ProcessZips
import argparse


# Erase all files in a directory
def EraseFiles(mydir):
    files = [f for f in os.listdir(mydir) if os.path.isfile(os.path.join(mydir, f))]
    for f in files:
        os.remove(os.path.join(mydir, f))
    return


### Usage LeumiMail Gmail-username Gmail-password PDF-passport [NoEmail]
parser = argparse.ArgumentParser(description='Process Leumi email from Gmail')
#parser.add_argument('gmailAccount', metavar='gmailAccount', type=str,
#                    help='the gmail account having the Leumi email in its Inbox')
parser.add_argument('-e', dest='gmailAccount', action='store',
                    help='the gmail account having the Leumi email in its Inbox')
parser.add_argument('-p', dest='Gpwd', action='store',
                    help='gmail account password')
parser.add_argument('-P', dest='Dpwd', action='store',
                    help='PDF files password')
parser.add_argument('-Nemail', dest='EmailProcess', action='store_false',  # By default - process email
                    help='When set-gmail is not accessed and recent files are used')
parser.add_argument('-downloaded', dest='downloaded', action='store_true',  # By default - not downloaded
                    help='When set-process messages that were donwloaded to downlowd folder')
parser.add_argument('-Z', dest='zipInp', action='store',
                    help='Folder of ZIP files')


if __name__ == '__main__':

    print 'LeumiMail Release 4.0'   #update release number

    MyArgs = vars(parser.parse_args())

    # create variables
    locals().update(MyArgs)

    workingDir = os.path.abspath('..\\temp')  # directory where to save attachments (default: current)
    emailsDir = os.path.abspath(workingDir + "\\emails")
    attachmentsDir = os.path.abspath(workingDir + "\\attachments")
    downloadedDir = os.path.abspath(workingDir + "\\downloaded")
    accountsFile = "ListOfAccounts.csv"

    # Interactive
    if downloaded or gmailAccount is None:
        EmailProcess = False
        if zipInp is None:
            zipsDir = os.path.abspath(workingDir + "\\zips")
        else:
            zipsDir = zipInp

    else:
        if EmailProcess:
            if Gpwd is None:
                Gpwd = getpass.getpass("Enter your gmail password: ")
        if Dpwd is None:
            Dpwd = getpass.getpass("Enter your Doc password: ")

    # Create the accounts table
    Accounts = Table()
    csv_fp = open('ListOfAccounts.csv', 'rb')
    Accounts.populate_Table(csv_fp)

    if (not downloaded) and gmailAccount is not (None):

        # login to gmail account and for a selected emails, extract the attachments

        ## Remove all files in the working environment
        if EmailProcess:
            print >> sys.stderr, 'parameters parsed %s, %s, %s, %r' % (gmailAccount, Gpwd[-3:], Dpwd[-4:], EmailProcess)
            EraseFiles(emailsDir)

            if DetachEmails(gmailAccount, Gpwd, workingDir + "\\emails", condition=[]):
                print >> sys.stderr, 'email logout'
            else:
                print >> sys.stderr, 'Processing aborted'
                exit(1)

        # each email attachment which is a PDF file, has its own attachment, usually HTML.
        # extract those
        EraseFiles(attachmentsDir)
        files = [f for f in os.listdir(emailsDir)]
        for f in files:
            extractembedded(f, password=Dpwd, extractdir=attachmentsDir, emailsDir=emailsDir)

        print >> sys.stderr, 'attachment extracted'
        # for each HTML - parse the file, identify the account and date, and rename the file accordingly

        ProcessHTML(Accounts, attachmentsDir)

        print "end processing - check temp\\attachments sub directories"

    else:

        # Process the ZIP files
        ProcessZips(zipsDir, downloadedDir)
        # process downloaded files
        ProcessHTML(Accounts, downloadedDir)
        origDir = os.getcwd()
        os.chdir(downloadedDir)
        files = [f for f in os.listdir('.') if (os.path.isfile(f) and os.path.splitext(f)[1].lower() == '.html')]
        for f in files:
            try:
                dst = 'Processed//' + f
                shutil.move(f, 'Processed\\' + f)#move
            except Exception as e:
                print >> sys.stderr, 'At cleanup couldn"t move from %s' % (f)


        print "end processing - check temp\\downloaded sub directories"

    exit(0)
