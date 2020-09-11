#! /bin/bash
####################################
#useradd                           #
#v1.0 mawc 18/4/2019               #           
####################################
read -p "please input number:" num
if [[ ! "$num" =~ ^[0-9]+$ ]];then   #正则表达式匹配数字 
	echo "error number."
	exit
fi

read -p "please input prefix:" prefix
if [ -z "$prefix" ];then
	echo "error prefix."
	exit
fi

for i in `seq $num`
do
	user=$prefix$i
	useradd $user
	echo "123456"
	if  [ $? -eq 0 ];then
		echo "$user is created.."
	fi
done
