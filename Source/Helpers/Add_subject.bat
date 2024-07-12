rem source for bat file. Actual one - save with "__" at the beginning of name
chcp 1255
set "gdr=G:\My Drive\0 Personal G\Banks\Bank Leumi"
rem in following set source OR peoduction in the path
call ..\.venv\Scripts\activate.bat
@echo on
set "acc=838-03400257 Joint"
set fold=%gdr%\%acc%
python Add_subject_PDF.py "%fold%" 1>"temp\logs\Add_subject_PDF_%acc%.log" 2>&1
type "temp\logs\Add_subject_PDF_%acc%.log"
pause


