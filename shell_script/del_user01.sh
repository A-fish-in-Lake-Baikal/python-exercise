#! /bin/bash
#delete user
#1.0 by mawc 2019.4.20

read -p "please input a username: " user

id $user &>/dev/null
if [ $? -ne 0 ];then
	echo "no such user:$user"
	exit
fi

read -p "Are you sure?[y/n]:" action
case "$action" in
y|Y|yes|YES)
	userdel -r $user &>/dev/null
	echo "$user is delete success..."
	;;
*)
	echo "exit delete program..."
esac
