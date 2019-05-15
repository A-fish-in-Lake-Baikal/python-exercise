#! /bin/bash

pc1=192.168.11.186
pc2=192.168.11.27

while :
do
	cat <<-EOF
	1.parrot
	2.deppin
	EOF

	read -p "please input number: " num
	case $num in
		1)
			echo "you choose parrot"
			;;
		2)
			echo "you choose deppin"
			;;
		"")
			echo "no choose,Please re-select"
			;;
		*)
			echo "input error,Please re-select"
	esac
done
