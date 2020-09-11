#! /usr/bin/zsh

ping -c10 www.baidu.com &>/dev/null && echo "www.baidu.com is up" || echo "www.baidu.com is down"



#这一块代码的意思是执行Python代码，‘<<-EOF 把代码指向解释器Python3，以EOF结束’
python3 <<-EOF

print("这是一句Python代码")

EOF
