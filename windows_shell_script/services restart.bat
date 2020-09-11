@echo ---------------------开始重启服务--------------------------- >> result.txt
date /t >> result.txt
time /t >> result.txt
@echo ------------------------------------------------------------ >> result.txt
net stop PsDataService >> result.txt
net start PsDataService >> result.txt
net stop PsEncodeService >> result.txt
net start PsEncodeService >> result.txt
net stop PsHttpTransferService >> result.txt
net start PsHttpTransferService >> result.txt
net stop PsMonitorService >> result.txt
net start PsMonitorService >> result.txt
net stop PsScheduleService >> result.txt
net start PsScheduleService >> result.txt
net stop PSStreamService >> result.txt
net start PSStreamService >> result.txt
net stop PsVodService >> result.txt
net start PsVodService >> result.txt
net stop PsUserService >> result.txt
net start PsUserService >> result.txt
@echo ---------------------重启结束--------------------------- >> result.txt