#! /bin/bash
# count tcp status

declare -A status

type=`ss -an | grep 0: | awk '{print $2}'`

for i in $type
do
	let status[$i]++
done

for j in ${!status[@]}
do
	echo "$j: ${status[$j]}"
done
