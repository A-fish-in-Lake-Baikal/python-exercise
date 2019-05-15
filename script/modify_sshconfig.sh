#! /bin/bash
#v1.0 by mawc

for ip in `cat ip.txt`
do
	{
		ping -c1 -W1 $ip &>/dev/null
		if [ $? -eq 0 ];then
			ssh $ip "sudo sed -ri '/^# UseDNS/cUseDNS no' /etc/ssh/sshd_config"
			ssh $ip "sudo sed -ri '/^GSSAPIAuthentication/cGSSAPIAuthentication no' /etc/ssh/sshd_config"
			ssh $ip "systemctl stop firewalld; systemctl disable firewalld"
		fi
	}&

done
wait
echo "all ok..."

