#! /bin/bash
while :
do
	read -p "please enter prefix & passwod & number[mawc 00000 01]: " prefix pass num
	printf "user infomation:
	--------------------------------------
	user prefix: $prefix
	user passwod: $pass
	user number: $num
	--------------------------------------
	"

	read -p "Are you sure[y/n]:" action
	if [ "$action" = "y" ];then
		echo "跳出循环，继续下面的操作"
		break
	fi
done

for i in `seq  $num`
do
	user=$prefix$i
	id $user &>/dev/null
	if [ $? -eq 0 ];then
		echo "user $user already exists"
	else
		useradd $user
		echo "$pass" |passwd --stdin $user &>/dev/null
		if [ $? -eq 0 ];then
			echo "$user is created."
		fi
	fi
done
echo "脚本执行完成。。。。"
