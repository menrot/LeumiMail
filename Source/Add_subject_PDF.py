# -*- coding: utf-8 -*-

"""
LeumiMail - Add subject to PDF existing file

    Release V1.0

    As more notices are now PDF, the subject of the notice will be added to already processed PDF notices.


    The program receives the following parameters

    [location]   folder to scan and rename PDF files




"""

import os
import argparse
import glob
import pdfplumber
import re


def get_subject(file):

    regex_subj = r'(?P<Subject>([א-ת]+ )+[א-ת]+)'
    re_subj = re.compile(regex_subj)

    subj = ''
    with pdfplumber.open(file) as pdf:
        # Extract the text
        pages = pdf.pages
        safe_text = pages[0].extract_text()

    detection, found = False, False

    for line in safe_text.split('\n'):
        # print(line)
        if not detection:
            if 'חוקל .סמ' in line:
                detection = True
            else:
                continue
        else:  # subject line
            match_subj = re_subj.search(line)
            subj = match_subj.group('Subject')[::-1]
            found = True
            break

    if not found:
        print('Subject not found in file %s' % file)

    return subj


parser = argparse.ArgumentParser(description='Add subject to file name of PDF files')

parser.add_argument('workingDir', nargs='?', default=os.getcwd(), action='store',
                    help='Folder to scan for PDF files')

if __name__ == '__main__':

    print('Add_subject_PDF 1.0')  # update release number

    MyArgs = vars(parser.parse_args())

    # create variables
    locals().update(MyArgs)

    # check if the directory exists
    if not os.path.exists(workingDir):
        print('Directory does not exist')
        exit(1)

    origDir = os.getcwd()
    os.chdir(workingDir)
    subject = ''

    # get all PDF files in the directory
    # files = [f for f in os.listdir(workingDir) if os.path.isfile(os.path.join(workingDir, f))]
    files = glob.glob('*.pdf')

    for f in files:
        # print(f)
        # get the subject of the file
        if len(os.path.basename(f)) > 37:  # there is already subject in file name
            continue
        if len(os.path.basename(f)) < 37:  # not a typical notice
            print('Not a typical notice file %s' % f)
            continue

        subject = get_subject(f)
        # rename the file
        try:
            os.rename(f, os.path.basename(f)[:-4] + ' ' + subject + '.pdf')
            # print('renamed to ' + os.path.basename(f)[:-4] + ' ' + subject + '.pdf')
        except Exception as e:
            print('Error renaming file %s' % f)
            print(e)

    os.chdir(origDir)
    print("end processing")

    exit(0)
