#! /usr/bin/zsh
#echo -e "\e[1;35m请输入要ping的ip：\e[1;0m"        输入提示语
#read -p "plese input a ip: " ip

ping -c1 $2 &>/dev/null
if [ $? -eq 0 ];then
	echo -e "\e[1;33m$2 is up"
else
	echo -e "\e[1;34m$2 is filed"
fi
