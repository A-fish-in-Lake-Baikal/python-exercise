#! /bin/sh
#system manage

menu() {
	cat <<-EOF
		+------------------------------------------------------+
		|                   Please a Tool  		               |
		|	h. help					                           | 
		|	f. disk partition			                       |
		|	d. filesystem mount		                           |
		|	m. memory				                           |
		|	u. system load				                       |
		|	n. install nginx			                       |		
		|	q. exit					                           |	
		+------------------------------------------------------+
	EOF
}
menu
while :
do
	read -p "please input [h for help]:" action
	case "$action" in
		h)
			clear
			menu
			;;
		f)
			fdisk -l
			;;
		d)
			df -Th
			;;
		m)
			free -m
			;;
		u)
			uptime
			;;
		n)
			echo "开始安装NGINX"
			dpkg -l | grep nginx
			if [ $? -eq 0 ];then
				status = 'systemctl status nginx'
				echo "nginx已经安装,版本为：$status"
			else
				sudo apt-get install nginx
			fi
		q)
		#	exit
			break
			;;
		"")
			;;
		*)
			echo "input error"
	esac
done
echo -e "\e[1;33mfinsh... \e[1;0m"
