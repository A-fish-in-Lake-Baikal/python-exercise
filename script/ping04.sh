#! /usr/bin/zsh

ip=www.baidu.com

ping -c1 $ip &>/dev/null
if [ $? -eq 0 ];then
	echo -e "\e[1;33m$ip is up"
else
	echo -e "\e[1;34m$ip is filed"
fi
