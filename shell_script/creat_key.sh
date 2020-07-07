#!/bin/bash

set -e

# 判断OpenSSL是否安装
# 。。。。。。



# 第一步：生成私钥
# 	genra	生成RSA私钥
# 	-des3	des3算法
# 	-out server.key 生成的私钥文件名
# 	2048 私钥长度
openssl genrsa -des3 -out server.pass.key 2048

# 第二步：去除私钥中的密码
openssl rsa -in server.pass.key -out server.key
rm -f server.pass.key

# 第三步：生成CSR(证书签名请求)
# req 生成证书签名请求
# -new 新生成
# -key 私钥文件
# -out 生成的CSR文件
# -subj 生成CSR证书的参数
SUBJ="$1"
# echo $SUBJ
openssl req -new -key server.key -out server.csr -subj "//O=Org\C=CN\ST=BeiJing\L=BeiJing\O=parasaga\OU=parasaga\CN=${SUBJ}"

# 第四步：生成自签名SSL证书
# -days 证书有效期
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
