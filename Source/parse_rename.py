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

def parse_notice(file, accounts, workingDir):

    origDir= os.getcwd()
    os.chdir(workingDir)
    f = open(file, 'r')

    BeautifulSoup("html5lib", "html.parser")
    soup = BeautifulSoup(f.read().decode('utf-8', 'ignore'))
    # search for customer number
    cue_word = u'חוקל'

    lines = string.split(soup.text, "\n")
    short_name = "Not Found"
    datePrefix = "00000000"
    for l in lines:
        if l.find(cue_word) > 0:
            c1 = l.find("/")
            cust_str = l[(c1-5):(c1+3)]
            r = accounts.lookup_Table(Customer=cust_str)
            if len(r) >0:
                short_name = r["ShortName"]
                break
        match = re.search(r'\d\d/\d\d/\d\d', l[0:8])
        if match:
            datePrefix = '20' + l[6:8] + l[3:5] + l[0:2] #20YYMMDD

    os.chdir(origDir)
    return (short_name, datePrefix)



if __name__ == '__main__':
    if len(sys.argv) <3:
        print "usage parse_rename file, workinDir"
        exit(1)
    else:
        Accounts = Table()
        csv_fp = open('ListOfAccounts.csv', 'rb')
        Accounts.populate_Table(csv_fp)
        cust_name, datePrefix = parse_notice(sys.argv[1], Accounts, sys.argv[2])
        print cust_name, datePrefix








