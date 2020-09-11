date /t >> result.txt
time /t >> result.txt
net stop MSSQLSERVER  /y >> result.txt
net start MSSQLSERVER >> result.txt