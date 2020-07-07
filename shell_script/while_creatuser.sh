#! /bin/bash

while read user
do
	id $user &>/dev/null
	if [ $? -eq 0 ];then
		echo "user $user already exists"
	else
		useradd $user
		if [ $? -eq 0 ];then
			echo "$user is created.."
		fi
	fi
done < user.txt
