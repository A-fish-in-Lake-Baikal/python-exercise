#! /bin/bash
#system manage

menu() {
	cat <<-EOF
		+------------------------------------------------------+
		|       Please a Tool				       |
		|	h. help					       | 
		|	f. disk partition			       |
		|	d. filesystem mount		               |
		|	m. memory				       |
		|	u. system load				       |	
		|	q. exit					       |	
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
