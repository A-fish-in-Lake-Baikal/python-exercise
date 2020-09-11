#!/bin/bash

set -e
# 判断OpenSSL是否安装
# 。。。。。。

# 提示用户输入域名，并判断输入是否为空
read -p "请输入证书的域名：" domain_name
if [ ! -n "$domain_name" ];then
	echo -e "\033[42;31m you have not input domain_name \033[0m"
	exit
else
	echo -e "the domain name is \033[31m $domain_name \033[0m"
fi

SUBJ="/C=CN/ST=BeiJing/L=BeiJing/O=parasaga/OU=parasaga/CN=${domain_name}"

# 第一步：生成私钥
# 	genra	生成RSA私钥
# 	-des3	des3算法
# 	-out server.key 生成的私钥文件名
# 	2048 私钥长度
#spawn openssl genrsa -des3 -out server.pass.key 2048
expect <<-EOF
spawn openssl genrsa -des3 -out server.pass.key 2048
expect "Enter pass phrase for server.pass.key:"
send "00000\r"
expect "Verifying - Enter pass phrase for server.pass.key:"
send "00000\r"
expect eof
EOF

# 第二步：去除私钥中的密码
expect <<-EOF
spawn openssl rsa -in server.pass.key -out server.key
expect "Enter pass phrase for server.pass.key:"
send "00000\r"
expect eof
EOF

rm -f server.pass.key

# 第三步：生成CSR(证书签名请求)
# req 生成证书签名请求
# -new 新生成
# -key 私钥文件
# -out 生成的CSR文件
# -subj 生成CSR证书的参数

# echo $SUBJ

openssl req -new -key server.key -out server.csr -subj ${SUBJ}

# 第四步：生成自签名SSL证书
# -days 证书有效期
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
