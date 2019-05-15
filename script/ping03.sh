#! /usr/bin/zsh

ip=www.baidu.com1

if ping -c1 $ip &>/dev/null;then
	echo -e "\e[1;33m$ip is up"
else
	echo -e "\e[1;34m$ip is filed"
fi
