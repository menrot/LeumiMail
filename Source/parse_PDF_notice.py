
import os, sys
import pdfplumber
import re
from MrUtils import Table
import pathlib


def parse_PDF_notice(file, accounts, workingDir, bank):
    origDir = os.getcwd()
    os.chdir(workingDir)

    regex2 = r'(?P<Date>\d\d\/\d\d\/\d\d) \d\d\-\d+\-(?P<Acc>\d+\/\d\d)'
    re2 = re.compile(regex2)

    regex3 = r'(?P<Page>\d [א-ת]+ \d [א-ת]+) \d\d\-\d+\-(?P<Acc>\d+\/\d\d)'
    re3 = re.compile(regex3)

    regex_subj = r'(?P<Subject>([א-ת]+ )+[א-ת]+)'
    re_subj = re.compile(regex_subj)

    regex_date = r'(?P<Date>\d+\/\d\d\/\d\d\d\d)'  # day in month can be single digit
    re_date = re.compile(regex_date)


    short_name = "Not Found"
    datePrefix = "00000000"
    subject = "Not Found"

    with pdfplumber.open(file) as pdf:
        # Extract the text
        pages = pdf.pages
        safe_text = pages[0].extract_text()

    loc = safe_text.find('חוקל .סמ')
    detection, old_format, new_format, new_format_line2, new_format_line3 = False, False, False, False, False

    for line in safe_text.split('\n'):
        # print(line)
        if not detection:
            if 'חוקל .סמ' in line:
                detection = True
                if 'דומע' in line: # it is new format
                    new_format_line2 = True
                    match3 = re3.search(line)
                    if match3:
                        cust_str = match3.group('Acc')
                        r = accounts.lookup_Table(Customer=cust_str)
                        if r is not None:
                            short_name = r["ShortName"]
                        else:
                            print('Account doesn"t exist in  file %s' % file, file=sys.stderr)
                            detection = False
                            break

                else: # old format date in the same line
                    old_format = True
                    match2 = re2.search(line[:-9])
                    if match2:
                        cust_str = match2.group('Acc')
                        r = accounts.lookup_Table(Customer=cust_str)
                        if r is not (None):
                            short_name = r["ShortName"]
                        else:
                            print('Account doesn"t exist in  file %s' % file, file=sys.stderr)
                            detection = False
                            break

                        date = match2.group('Date')
                        datePrefix = '20' + date[6:8] + date[3:5] + date[0:2]  # 20YYMMDD

                    # end old format
            else:
                continue
        elif old_format:
            match_subj = re_subj.search(line)
            subject = match_subj.group('Subject')[::-1] # reverse order
            old_format = False # stop parsing this document
            break
        elif new_format_line2:
            match_subj = re_subj.search(line)
            if match_subj:
                subject = match_subj.group('Subject')[::-1] # reverse order

            new_format_line2 = False
            new_format_line3 = True
            continue
        elif new_format_line3:
            match_date = re_date.search(line)
            if match_date:
                date = match_date.group('Date')
                if len(date) == 9: # single digit day in month, add zero preceding it
                    date2 = '0' + date
                    date = date2

                datePrefix = date[6:10] + date[3:5] + date[0:2]
            new_format_line3 = False
            break

    os.chdir(origDir)
    if not detection:
        print('No cue word in file %s' % file, file=sys.stderr)
        return short_name, datePrefix, subject
    else:
        # print('Cue word found in file %s' % file)
        # print(short_name, datePrefix, subject)
        return short_name, datePrefix, subject


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("usage parse_PDF_notice workinDir file bank")
        exit(1)
    else:
        Accounts = Table()
        csv_fp = open('ListOfAccounts.csv', 'rt')
        Accounts.populate_Table(csv_fp)

        if len(sys.argv) == 4:
            cust_name, datePrefix, subject = parse_PDF_notice(sys.argv[2], Accounts, sys.argv[1], int(sys.argv[3]))
            print(cust_name, datePrefix, subject)
        elif len(sys.argv) == 3:  # process the whole folder
            files = [f for f in os.listdir(sys.argv[1])]
            for f in files:
                if (pathlib.Path(f).suffix).lower()[1:] == 'pdf':
                    cust_name, datePrefix, subject = parse_PDF_notice(f, Accounts, sys.argv[1], sys.argv[2])
                    print(cust_name, datePrefix, subject, f)
        exit(0)
