#! /bin/bash
#判断用户是否输入参数
if [ $# -eq 0 ];then
	echo "没有输入参数，请重新输入！"
	exit 1
fi
#判断用户输入的是否是文件
if [ ! -f $1 ];then
	echo "error file"
	exit 2
fi
#for处理文件默认按照回车分割
#所以需要重新定义分隔符
#IFS=$'\n'
IFS='
'
for line in `cat $1`
do
	if [ ${#line} -eq 0 ];then
		echo "nothing to do"
		continue
	fi
	user=`echo "$line" |awk '{print $1}'`
	passwd=`echo "$line" |awk '{print $2}'`
	echo "用户：$user"
	echo "密码：$passwd"
done

echo "脚本执行完成。。。。"
