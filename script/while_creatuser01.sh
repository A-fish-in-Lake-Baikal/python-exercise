#! /bin/bash

while read line
do
	user=`echo $line|awk '{print $1}'`
	pass=`echo $line|awk '{print $2}'`
	id $user &>/dev/null
	if [ $? -eq 0 ];then
		echo "user $user already exists"
	else
		echo "$user : $pass"
	fi
done < $1
