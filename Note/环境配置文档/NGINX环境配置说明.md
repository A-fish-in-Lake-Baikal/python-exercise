# NGINX环境配置说明
## 环境要求说明
```Text
	操作系统版本：Ubuntu18.04
	NGINX版本：最新的稳定版本
```
## 安装配置步骤
~~~Bash
	1. 安装nginx（参考视频nginx安装）
		$ sudo apt-get install nginx
	2. 将证书拷贝到服务器上home目录下
	3. 进入NGINX安装目录
		$ sudo cd /etc/nginx/
	4. 创建文件夹“sites”
	5. 将cqweb.conf上传到sites，并且配置参数（配置内容较多，请仔细查看注释进行配置）
	6. 修改NGINX配置文件(如下图)
        $ sudo vim /etc/nginx/nginx.conf
~~~
![NGINX配置文件](https://i.loli.net/2020/08/18/r8xhqO9wXUM4zQR.png)
~~~Bash
	7. 重启nginx
		$ sudo systemctl restart nginx
	8. 开启防火墙
		$ sudo ufw enable
	9. 根据实际情况将服务器的端口打开
		$ sudo ufw allow 443   #例子
	10. 查看防火墙状态和已经打开的端口
		$ sudo ufw status
~~~
## 云平台映射
~~~Text
1. 2.3.2的版本需要替换补丁，详见钉盘文件。
2. 配置云平台映射，如图
~~~

![云平台映射](https://i.loli.net/2020/08/18/lAeZcW4Gxwj1KI6.jpg)
~~~
Upload：一般是443对应云平台的1660
HttpSteaming：对应的是云平台的1670端口，用来播放http协议的资源
HttpsSteaming：对应的也是云平台的1670端口，所有的https链接都走的这个协议
Parasaga：对应的是云平台的1680端口，用来播放未转码的资源，不通过NGINX映射
~~~
<font color=#FF0000 size=4>    注意：</font>
<font color=#FF0000 size=4>    1. 有CDN服务器的需要在NGINX和云平台添加对应的映射，不然会导致缓存的资源无法播放</font>
<font color=#FF0000 size=4>	 2. 如果域名和公网ip同时使用，则需要同时映射</font>