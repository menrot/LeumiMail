# -*- coding: utf-8 -*-

## parse and Leumi HTML file and rename
## account_name, date, id in date
##

from __future__ import division, unicode_literals
from bs4 import BeautifulSoup
import os, sys
import string
import re
from MrUtils import Table

<<<<<<< HEAD

def parse_notice(file, accounts, workingDir):
    origDir = os.getcwd()
=======
def parse_notice(file, accounts, workingDir):

    origDir= os.getcwd()
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
    os.chdir(workingDir)
    f = open(file, 'r')

    soup = BeautifulSoup(f.read().decode('utf-8', 'ignore'), 'html.parser')
    # search for customer number
    cue_word = u'חוקל'

    # soup.get_text("|", strip=True)
    lines = string.split(soup.text, "\n")
    short_name = "Not Found"
    datePrefix = "00000000"
    line_nr = 0
    for l in lines:
        if l.find(cue_word) > 0:
            span = [x.span() for x in re.finditer(r'\d*\d\d\d\d\d/\d\d', l)]
            cust_str = l[span[0][0]:span[0][1]]
            r = accounts.lookup_Table(Customer=cust_str)
<<<<<<< HEAD
            if r is not(None):
=======
            if len(r) >0:
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
                short_name = r["ShortName"]
                line_nr = lines.index(l)
                line_nr_seek = 1
                span = [x.span() for x in re.finditer(r'\d\d/\d\d/\d\d', l)]
                while not span:
                    # search for date in previous lines
<<<<<<< HEAD
                    l = lines[line_nr - line_nr_seek]
=======
                    l = lines[line_nr-line_nr_seek]
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
                    if line_nr_seek > 5:
                        break
                    else:
                        line_nr_seek = line_nr_seek + 1
                        span = [x.span() for x in re.finditer(r'\d\d/\d\d/\d\d', l)]

                if span:
                    match = l[span[0][0]:span[0][1]]
                    datePrefix = '20' + match[6:8] + match[3:5] + match[0:2]  # 20YYMMDD
                else:
<<<<<<< HEAD
                    print >> sys.stderr, 'Parsing the date failed in file %s' % file
                break
            else:
                print >> sys.stderr, 'Account doesn"t exist in  file %s' % file
=======
                    print >>sys.stderr, 'Parsing the date failed in file %s' % file
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
                break


    os.chdir(origDir)
    return (short_name, datePrefix)


<<<<<<< HEAD
if __name__ == '__main__':
    if len(sys.argv) < 3:
=======

if __name__ == '__main__':
    if len(sys.argv) <3:
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
        print "usage parse_rename file, workinDir"
        exit(1)
    else:
        Accounts = Table()
        csv_fp = open('ListOfAccounts.csv', 'rb')
        Accounts.populate_Table(csv_fp)
        cust_name, datePrefix = parse_notice(sys.argv[1], Accounts, sys.argv[2])
        print cust_name, datePrefix
<<<<<<< HEAD
=======









>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
