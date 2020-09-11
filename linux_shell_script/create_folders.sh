#! /bin/sh
dir=vmsd-168-`date |awk '{print $6}'`-`date |awk '{print $2}'`-`date |awk '{print $3}'`
creat(){
	echo -e "\e[1;31m开始创建新的$dir....\e[0m"
	mkdir vmsd
	find /vmfs -name "*.vmsd" -exec cp {} --parents /vmsd/ \;
	if [ $? -eq 0 ];then
		mv vmsd $dir
		echo -e "\e[1;32m新的$dir文件夹成功生成！\e[0m"
	fi
}

ls | grep vmsd-* &>dev/null
if [ $? -eq 0 ];then
	echo -e "\e[1;33m存在旧的快照文件夹，开始删除.....\e[0m"
	rm -rf vmsd-*
	if [ $? -eq 0 ];then
		echo -e "\e[1;34m旧的$dir文件夹成功删除！\e[0m"
		creat
	fi
else
	echo -e "\e[1;35m不存在旧的快照文件夹\e[0m"
	creat
fi
