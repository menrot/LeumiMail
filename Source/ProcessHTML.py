# -*- coding: utf-8 -*-

import sys, os
from parse_rename import parse_notice
import webbrowser
import pymsgbox
from shutil import copyfile
from MrUtils import Table
import pathlib


def ProcessHTML(Accounts, noticesDir):
    origDir = os.getcwd()
    os.chdir(noticesDir)
    Save_all = False
    files = [f for f in os.listdir('.') if os.path.isfile(f)]  # exclude directories
    for f in files:
        if (pathlib.Path(f).suffix).lower()[1:] == 'html':
            acc_name, date_pref = parse_notice(f, Accounts, '.')
            if not (acc_name == "Not Found" or date_pref == "00000000"):
                # It is a standard notice
                ordinal = f.find("Attachment")
                if ordinal > 0:
                    ordinal = f[ordinal + 11:ordinal + 12]
                    filename_base = False
                else:
                    # append to file name, dont replace  the name
                    ordinal = 0
                    filename_base = pathlib.Path(f).stem.lower()
                DisplayText = "Account: {0} \nDate: {1}".format(acc_name, date_pref)
                if not Save_all:
                    webbrowser.open(f, new=0)
                    response = pymsgbox.confirm(text=DisplayText, title='Confirm to save',
                                            buttons=['Save', 'Ignore', 'Mark', 'Save All'])
                    if response == 'Save All':
                        Save_all = True
                        response = 'Save'
                else:
                    response = 'Save'
                if response == "Save" or response == "Mark":
                    if not os.path.exists(acc_name):
                            os.makedirs(acc_name)
                    if ordinal > 0:
                        newF = '{0} {1}'.format(date_pref, ordinal)
                    else:
                        newF = '{0} {1}'.format(date_pref, filename_base)
                    while os.path.exists(os.path.join(acc_name, '{0}.html'.format(newF))):
                        try:
                            print ('Target file %s exists. Creating it again with ordinal' % newF, file=sys.stderr)
                        except (Exception, e):
                            print  ('%s Target file %s exists. Creating it again with ordinal' % (str(e), newF), file=sys.stderr)
                        ordinal = str(int(ordinal) + 1)
                        if filename_base:
                            newF = '{0} {1} {2}.html'.format(date_pref, ordinal, filename_base)
                        else:
                            newF = '{0} {1}'.format(date_pref, ordinal)

                        if int(ordinal) > 9:
                            print ('Target name range exists for %s, ordinal %s in %s' % (
                                f, ordinal, acc_name), file=sys.stderr)
                            ordinal = 'check this one'
                            break

                    if response == "Mark":
                       newF = '{0} UPDATE NAME'.format(newF)
                    newF = '{0}.html'.format(newF)
                    try:
                        copyfile(f, os.path.join(acc_name, newF))
                            # print ('copyfile from %s to %s in %s' % (f, newF, acc_name), file=sys.stderr)
                    except Exception as e:
                            print ('Couldn"t copy from %s to %s in %s' % (f, newF, acc_name), file=sys.stderr)

                else:
                     print ('You asked not to save  %s' % f, file=sys.stderr)
            else:
                print ("Parsing of %s failed" % f, file=sys.stderr)
        else: #not HTML
            print ('Not a HTML %s' % f)
    os.chdir(origDir)
    return



if __name__ == '__main__':
    workingDir = '..\\temp'  # directory where to save attachments (default: current)
    emailsDir = workingDir + "\\emails"
    noticesDir = workingDir + "\\attachments"
    downloadedDir = workingDir + "\\downloaded"
    accountsFile = "ListOfAccounts.csv"

    Accounts = Table()
    csv_fp = open(accountsFile, 'rb')
    Accounts.populate_Table(csv_fp)

    if len(sys.argv) == 2: # process from downloadedDir
        ProcessHTML(Accounts, downloadedDir)
    else:
        ProcessHTML(Accounts, noticesDir)

