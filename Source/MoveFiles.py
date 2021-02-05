# -*- coding: utf-8 -*-

"""
LeumiMail move files to destination

    Move the files  from the project directory to the target folders



"""

import sys, os, shutil
from MrUtils import Table
import argparse


def moveFiles(src, dst):
    oDir = os.getcwd()
    os.chdir(src)
    files = [f for f in os.listdir('.') if (os.path.isfile(f) and
                                            (os.path.splitext(f)[1].lower() == '.html'
                                             or os.path.splitext(f)[1].lower() == '.pdf'))]
    for f_s in files:
        try:
            d = (dst + '\\' + f_s).encode('UTF-8')
            f = f_s.encode('UTF-8')
            ## print('Moving from %s, %s to %s ' % (src, f, d))  # move
            shutil.move(f, d)  # move
        except Exception as e:
            print('Couldn"t move %s %s because %s' % (src, f, e), file=sys.stderr)
    os.chdir(oDir)


### Usage MoveFiles.py CSV-file
parser = argparse.ArgumentParser(description='Copy Leumi notifications to target folders')
parser.add_argument('CSVfile', metavar='CSVfile', type=str,
                    help='The CSV file containing all the folders')
parser.add_argument('-D', dest='Drive', action='store',
                    help='G Drive local location')

if __name__ == '__main__':

    print('Move Files for Leumi')  # update release number

    MyArgs = vars(parser.parse_args())

    # create variables
    locals().update(MyArgs)

    workingDir = os.path.abspath('..\\temp')  # directory where to save attachments (default: current)
    downloadedDir = os.path.abspath(workingDir + "\\downloaded")
    if CSVfile != '':
        accountsFile = CSVfile
    else:
        accountsFile = "ListOfAccounts.csv"

    # Create the accounts table
    Accounts = Table()
    csv_fp = open(accountsFile, 'rt')
    Accounts.populate_Table(csv_fp)

    origDir = os.getcwd()
    os.chdir(downloadedDir)

    for j in Accounts:
        moveFiles(j['ShortName'], Drive + '\\' + j['TargetFolder'])

    print("end processing")

    exit(0)
