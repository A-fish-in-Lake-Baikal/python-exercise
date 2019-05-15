#! /bin/bash
# app install

dpkg-query -l ftp
if [ $? -eq 0 ];then
	echo -e "\e[1;34m该软件已经安装\e[1;0m"
else
	echo -e "\e[1;35m该软件未安装\e[1;0m"
	echo -e "\e[1;36m下面开始安装。。。\e[1;0m"
	sudo apt-get install ftp
fi
