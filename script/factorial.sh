#! /bin/bash
factorial(){
	factorial=1
	for ((i=1;i<=$1;i++))
	do
		factorial=$[$factorial * $i]
	done
	echo "$1的阶乘是：$factorial"
}

factorial $1
factorial $2
factorial $3
