#! /bin/bash

ip=www.baidu.com

i=1
while [ $i -le 5 ]
do
	ping -c1 $ip  &>/dev/null
	if [ $? -eq 0 ]; then
		echo "$ip is up..."
	else
		echo "$ip is down..."
	fi
	let i++
done
