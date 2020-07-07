#! /bin/bash
#批量向目标主机推送公钥
>ip_new.txt
passwd=00000
for i in {2..254}
do
	{
		ip=192.168.11.$i
		ping -c1 -W1 $ip &>/dev/null
		if [ $? -eq 0 ];then
			echo "$ip" >>ip_new.txt
			expect <<-EOF
			spawn ssh-copy-id $ip
			expect{
				"yes/no" { send "yes\r"; exp_confinue }
				"password:" { send "$passwd\r" }
			}
			expect eof
			EOF
		fi
	}&
done
wait
echo "finsh...."
