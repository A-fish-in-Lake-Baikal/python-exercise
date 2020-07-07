#! /bin/bash
for ip in `cat ip.txt`
do
	ping -c1 -W1 $ip &>/dev/null
	if [ $? -eq 0 ];then
		echo "$ip is up"
	else
		echo "$ip is down"
	fi
done
