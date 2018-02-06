# -*- coding: utf-8 -*-

"""LeumiMail - reads, displays and organizes Leumi notification.

    Function parameters should be documented in the ``Args`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    If \*args or \*\*kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name (type): description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        param1 (str): Gmail account name

        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """

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
parser.add_argument('-Nemail', dest='EmailProcess', action='store_false',  # By default - process email
                    help='When set-gmail is not accessed and recent files are used')
parser.add_argument('-downloaded', dest='downloaded', action='store_true',  # By default - not downloaded
                    help='When set-process messages that were donwloaded to downlowd folder')

MyArgs = vars(parser.parse_args())

# create variables
locals().update(MyArgs)

# Interactive
if downloaded:
    EmailProcess = False
else:
    if EmailProcess:
        if Gpwd is None:
            Gpwd = getpass.getpass("Enter your gmail password: ")
    if Dpwd is None:
        Dpwd = getpass.getpass("Enter your Doc password: ")

workingDir = '..\\temp'  # directory where to save attachments (default: current)
emailsDir = workingDir + "\\emails"
attachmentsDir = workingDir + "\\attachments"
downloadedDir = workingDir + "\\downloaded"
accountsFile = "ListOfAccounts.csv"

# Create the accounts table
Accounts = Table()
csv_fp = open('ListOfAccounts.csv', 'rb')
Accounts.populate_Table(csv_fp)

if (not downloaded):

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
    # process downloaded files
    ProcessHTML(Accounts, downloadedDir)
    print "end processing - check temp\\downloaded sub directories"

exit(0)

# Open each file, and if approved - move to target folder based on account name
