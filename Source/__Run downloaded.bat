chcp 1255
LeumiMail.py -Z "D:\Users\Menashe\mG Drive\WinSysFolders\Downloads" 1>LeumiMailProcess.log 2>&1
type LeumiMail.log
echo ***** Ctrl^C if want to abort or SPACE to move files to fnal destination
pause
movefiles.py ListOfAccounts.csv -D="D:\Users\Menashe\mG Drive" 1>LeumiMailMove.log 2>&1