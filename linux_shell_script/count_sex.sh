#! /bin/bash
#利用数组统计某一种类型的数量
#把要统计的对象作为数组的索引
declare -A sex

while read line
do
	type=`echo $line |awk '{print $2}'`
	let sex[$type]++
done <sex.txt

for i in ${!sex[@]}
do
	echo "$i: ${sex[$i]}"
done
