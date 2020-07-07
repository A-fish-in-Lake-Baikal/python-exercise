#! /bin/sh
dir=vmsd
creat(){
	mkdir $dir
	find /vmfs -name "*.vmsd" -exec cp {} --parents /vmsd/ \;
	if [ $? -eq 0 ];then
		echo "新的$dir文件夹成功生成！"
	fi
}
if [ -d "./vmsd" ];then
	
	read -p "是否删除旧的$dir文件夹[y/n]:" action
	case $action in
	y|Y)
		rm -rf $dir
		if [ $? -eq 0 ];then
			echo "旧的$dir文件夹成功删除！"
			creat
		fi
		;;
	n|N)
		echo "Cancel deletion, exit ..."
		exit 0
	esac
else
	echo "$dir不存在，开始创建...."
	creat
fi
