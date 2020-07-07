#! /bin/bash

mem_used=`free -m | grep '^内存' |awk '{print $3}'`
mem_total=`free -m | grep '^内存' |awk '{print $2}'`
mem_percent=$((mem_used*100/mem_total))

echo "已用内存：$mem_used"
echo "总内存：$mem_total"
echo "当前系统内存使用百分比：$mem_percent"
