rem source for bat file. Actual one - save with "__" at the beginning of name
chcp 1255
set "gdr=G:\My Drive"
rem in following set source OR peoduction in the path
set "dwn=%gdr%\MrProjects\LeumiMail\source\temp\zips"
call ..\.venv\Scripts\activate.bat
@echo on
python LeumiMail.py -Z "%dwn%" -B Leumi 1>LeumiMailProcess.log 2>&1
type LeumiMailProcess.log
echo ***** Ctrl^C if want to abort or SPACE to move files to final destination
pause
python movefiles.py ListOfAccounts.csv -D="%gdr%" 1>LeumiMailMove.log 2>&1
type LeumiMailMove.log
pause
