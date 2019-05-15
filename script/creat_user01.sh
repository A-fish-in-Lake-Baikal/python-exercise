#! /bin/bash
####################################
#useradd                           #
#v1.0 mawc 18/4/2019               #           
####################################
read -p "please input number:" num
read -p "please input prefix:" prefix

for i in `seq $num`
do
	user=$prefix$i
	useradd $user
	echo "123456"
	if  [ $? -eq 0 ];then
		echo "$user is created.."
	fi
done
