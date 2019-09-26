#! /bin/sh

menu() {
	cat <<-EOF
	+-----------------------------+
	+          tools box          +
	+   r. nginx restart          +
	+   v. nginx version          +
	+   s. nginx status           +
	+   d. remove nginx           +
	+   n. install nginx          +
	+   u. update nginx           +
	+   h. help                   +
	+   q. exit                   +
	+-----------------------------+
	EOF
}


up() {
	dpkg -l | grep sed
	if [ $? -eq 0 ];then
		echo "sed已安装"
	else
		sudo apt-get install sed
	fi
	sour1='$a\deb [arch=amd64] http://nginx.org/packages/mainline/ubuntu/ bionic nginx'
	sour2='$a\deb-src http://nginx.org/packages/mainline/ubuntu/ bionic nginx'
	sudo sed -i "$sour1" /etc/apt/sources.list
	sudo sed -i "$sour2" /etc/apt/sources.list
	sudo apt-get update
}

remove() {
	mod=`dpkg --get-selections | grep nginx | awk '{print $1}'`
	for line in $mod
	do
		sudo apt-get --purge remove $line
	done
#	sudo apt remove nginx nginx-common nginx-full nginx-core
}

while :
do
	menu
	read -p "please input [h for help]:" action
	case "$action" in
		r)
			systemctl restart nginx
			;;
		v)
			nginx -V
			;;
		s)
			systemctl status nginx
			;;
		d)
			remove
			;;
		n)
			echo "开始检查NGINX是否安装"
			dpkg -l | grep nginx
			if [ $? -eq 0 ];then
				echo "\e[1;31mNGINX已经安装\e[1;0m"
				nginx -V
			else
				echo  "\e[1;31mnginx没有安装,开始安装....\e[1;0m"
				up
				sudo apt-get install nginx
			fi
			;;
		u)
			echo "\e[1;31m----------开始升级NGINX----------\e[1;0m"
			up
			wget http://nginx.org/keys/nginx_signing.key
			sudo apt-key add nginx_signing.key
			remove
			sudo apt-get install nginx
			;;
		h)
			echo  "\e[1;31m----------使用说明----------\e[1;0m"
			echo  "\e[1;31m(r)重启NGINX\e[1;0m"
			echo  "\e[1;31m(v)查看NGINX版本\e[1;0m"
			echo  "\e[1;31m(d)卸载NGINX\e[1;0m"
			echo  "\e[1;31m(s)查看NGINX状态\e[1;0m"
			echo  "\e[1;31m(n)安装NGINX\e[1;0m"
			echo  "\e[1;31m(u)升级NGINX\e[1;0m"
			echo  "\e[1;31m(q)退出\e[1;0m"
			;;
		q)
			break
			;;
		"")
			;;
		*)
			echo  "\e[1;31minput error\e[1;0m"
	esac
done
