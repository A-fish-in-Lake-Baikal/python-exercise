#! /bin/bash
#ping check

>ip_test.txt
for i in {1..254}
do
	{
	ip=192.168.11.$i
	ping -c1 -W1 $ip &>/dev/null
	if [ $? -eq 0 ];then
		echo "$ip" |tee -a ip_test.txt
	fi
	}&
done
wait
echo "finish..."
