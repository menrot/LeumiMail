# -*- coding: utf-8 -*-

"""
LeumiMail

    Release V6.0
    This module is to parse and organize notices from Leumi

    The program relies on downloading the internal Leumi inbox.
    These ZIP file contain HTML and PDF  members

    The program receives the following parameters

    -Z [location]   where the zip files exists

    The folder environment is as follows:
        script
        temp
            zips
            downloaded
                account_1
                account_2

    In the script folder there has to be a CSV file describing the accounts



"""

import os
from MrUtils import Table
from ProcessNotice import ProcessNotice
from MrZip import ProcessZips
import argparse
from enum import Enum


'''
decapitated
class BankEnum(Enum):
    """
    ENUM to hold the allowed values for banks
    """
    Leumi: int = 0
    Union: int = 1
'''

# Erase all files in a directory
def EraseFiles(mydir):
    files = [f for f in os.listdir(mydir) if os.path.isfile(os.path.join(mydir, f))]
    for f in files:
        os.remove(os.path.join(mydir, f))
    return


parser = argparse.ArgumentParser(description='Process Leumi messages')

parser.add_argument('-downloaded', dest='downloaded', action='store_true',  # By default - not downloaded
                    help='When set-process messages that were donwloaded to downlowded folder')
parser.add_argument('-Z', dest='zipInp', action='store',
                    help='Folder of ZIP files')
'''
decapitated
parser.add_argument('-B', dest='bank', action='store',
                    help='bank (Leumi or Union')
'''


if __name__ == '__main__':

    print('LeumiMail Release 6.2')  # update release number

    MyArgs = vars(parser.parse_args())

    # create variables
    locals().update(MyArgs)

    workingDir = os.path.abspath('.\\temp')  # directory where to save data files (default: current)
    downloadedDir = os.path.abspath(workingDir + "\\downloaded")
    accountsFile = "ListOfAccounts.csv"

    # Set parameters
    if zipInp is None:
        zipsDir = os.path.abspath(workingDir + "\\zips")
    else:
        zipsDir = zipInp



    # Create the accounts table
    Accounts = Table()
    csv_fp = open(accountsFile, 'rt')
    Accounts.populate_Table(csv_fp)

    # Process the ZIP files
    ProcessZips(zipsDir, downloadedDir)
    # process downloaded files
    ProcessNotice(Accounts, downloadedDir, 0)

    origDir = os.getcwd()
    os.chdir(downloadedDir)

    print("end processing - check temp\\downloaded sub directories")

    exit(0)
