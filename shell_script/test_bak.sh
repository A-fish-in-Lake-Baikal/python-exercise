#! /bin/bash

back_dir=/var/mysql_back

if [ !  -d $back_dir ]; then
	echo "该目录不存在..."
fi

echo "开始备份..."
