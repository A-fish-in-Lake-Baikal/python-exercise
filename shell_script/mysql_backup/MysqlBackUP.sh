#!/bin/bash
# Mysql本地以及远程备份
# Author:Mawc

# 查找备份文件
#find /etc/mysql/databackup/* -type f -m time+10 -name ".gz" -exec rm {}\;

# 主机地址
db_host="localhost"
# 数据库用户名
db_user="root"
# 数据库用户名密码
db_passwd="test12#$%"
# mysql安装目录
MYSQL="/etc/mysql"
# mysqldump命令所在目录
MYSQLDUMP="/usr/bin/mysqldump"
# 存放备份文件的路径
BackUp_DB="/etc/mysql/databackup/"
LogFile=$BackUp_DB"/back.log"
# 远程服务器存储路径
Remote_Path="/home/parasaga/databackup/"
# 远程主机用户名
Remote_user="root"
# 远程主机地址
Remote_host="192.168.3.196"


# 时间
time=`date "+%Y-%m-%d-%H-%M-%S"`
day=`date "+%d"`
month=`date "+%Y-%m"`
weekday=`date "+%u"`

# 备份文件
#Date=`date "+%Y%m%d"`
Begin=`date "+%Y-%m-%d %H:%M:%S"`

# 要备份的数据库名称，用,隔开
databaseList="psmp,psgep"
for databaseName in `echo "$databaseList" | sed 's/,/\n/g'`
do
	fileName=$databaseName"-"$time".sql"
	BACKUP_DBPATH=${BackUp_DB}${databaseName}
        # 判断备份文件夹是否存在，不存在则创建
	if [ ! -d "$BACKUP_DBPATH" ];then
		mkdir -p "$BACKUP_DBPATH"
	fi
	# 开始备份文件
	$MYSQLDUMP -u $db_user -p"$db_passwd" -h $db_host $databaseName > ${BACKUP_DBPATH}/${fileName}
	echo -e "["${Begin}"] 文件已经备份到："${BACKUP_DBPATH}/${fileName} >> ${LogFile}
done
# 删除多余的备份文件
python deleteFiles.py >> ${LogFile}

 # 删除多余的备份文件(先删除多余的文件，然后再远程备份)


# 远程传输备份文件（相当于同步文件夹，两个文件夹内的文件内容一致）
# scp -r ${BackUp_DB} root@${Remote_host}:${Remote_Path}
echo "["${Begin}"] -----开始远程增量备份-----" >> ${LogFile}
rsync -avzh --delete ${BackUp_DB}  ${Remote_user}@${Remote_host}:${Remote_Path} >> ${LogFile}
echo "["${Begin}"] -----远程备份结束-----" >> ${LogFile}
echo -e "\e[1;32m完成!... \e[0m"
# rsync -avz --delete /etc/mysql/databackup/  root@192.168.3.174:/home/parasaga/databackup/
