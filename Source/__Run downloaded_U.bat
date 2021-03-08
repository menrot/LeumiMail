chcp 1255
python LeumiMail.py -Z "D:\Users\Menashe\mG Drive\WinSysFolders\Downloads" -B Union 1>LeumiMailProcess.log 2>&1
type LeumiMailProcess.log
echo ***** Ctrl^C if want to abort or SPACE to move files to fnal destination
pause
python movefiles.py ListOfAccounts.csv -D="D:\Users\Menashe\mG Drive" 1>LeumiMailMove.log 2>&1
type LeumiMailMove.log
pause
