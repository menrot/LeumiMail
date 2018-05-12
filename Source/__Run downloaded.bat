chcp 1255
LeumiMail.py -Z "D:\Users\Menashe\G Drive\WinSysFolders\Downloads" 1>LeumiMail.log 2>&1
type LeumiMail.log
***** Ctrl^C if want to abort or SPACE to move files to fnal destination
pause
movefiles.py ListOfAccounts.csv -D="D:\Users\Menashe\G Drive"
