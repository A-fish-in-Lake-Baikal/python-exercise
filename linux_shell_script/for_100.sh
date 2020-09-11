#! /bin/bash

for i in {1..100}
do
	let sum=$sum+$i
done
echo "sum:$sum"
