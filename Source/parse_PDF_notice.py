
import os, sys
from tika import parser # pip install tika
import re
from MrUtils import Table
import pathlib




def parse_PDF_notice(file, accounts, workingDir):
    origDir = os.getcwd()
    os.chdir(workingDir)

    regex2 = r'\d\d\-\d\d\d\-(?P<Acc>\d+\/\d\d)(?P<Date>\d\d\/\d\d\/\d\d)'
    re2 = re.compile(regex2)

    short_name = "Not Found"
    datePrefix = "00000000"

    raw = parser.from_file(file)

    if 'content' in raw:
        text = raw['content']

        # Convert to string
        text = str(text)
        # Ensure text is utf-8 formatted
        safe_text = text  # .encode('utf-8', errors='ignore')

        loc = safe_text.find('מס. לקוח')

        if loc > 0:
            temp_str = safe_text[loc - 24:loc]
            match = re2.search(temp_str)
            if match:
                cust_str = match.group('Acc')
                r = accounts.lookup_Table(Customer=cust_str)
                if r is not (None):
                    short_name = r["ShortName"]
                else:
                    print('Account doesn"t exist in  file %s' % file, file=sys.stderr)

                date = match.group('Date')
                datePrefix = '20' + date[6:8] + date[3:5] + date[0:2]  # 20YYMMDD
            else:
                print('Parsing failed in file %s' % file, file=sys.stderr)
        else:
            print('No cue word in file %s' % file, file=sys.stderr)

    os.chdir(origDir)
    return short_name, datePrefix


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("usage parsw_PDF_notice workinDir file")
        exit(1)
    else:
        Accounts = Table()
        csv_fp = open('ListOfAccounts.csv', 'rt')
        Accounts.populate_Table(csv_fp)

        if len(sys.argv) == 3:
            cust_name, datePrefix = parse_PDF_notice(sys.argv[2], Accounts, sys.argv[1])
            print(cust_name, datePrefix)
        elif len(sys.argv) == 2:  # process the whole folder
            files = [f for f in os.listdir(sys.argv[1])]
            for f in files:
                if (pathlib.Path(f).suffix).lower()[1:] == 'pdf':
                    cust_name, datePrefix = parse_PDF_notice(f, Accounts, sys.argv[1])
                    print(cust_name, datePrefix, f)
        exit(0)
