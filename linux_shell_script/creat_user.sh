#! /bin/bash

read -p "please input a username:" user

id $user &>/dev/null
if [ $? -eq 0 ];then
	echo "user $user already exists.."
else
	sudo useradd $user
	if [ $? -eq 0 ];then
		echo "$user is created.."
	fi
fi

