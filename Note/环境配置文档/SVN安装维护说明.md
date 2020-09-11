# SVN维护

## 服务器说明：
~~~Text
    Ubuntu版本：18.04.3
    机器名称：Redmine
    机器IP：192.168.1.98
    机器所在服务器：19.2.168.1.168
    用户名：root
    密码：Test12#$%198
    MySQL版本：Ver 14.14 Distrib 5.7.31
    SVN版本：1.9.7 (r1800392)
    SVN所在路径：/root/svn
    SVN仓库名称：usercase
~~~

## 安装
###     安装步骤说明
~~~Bash
	1. 一般情况下Ubuntu系统自带SVN，可以使用以下命令检查一下是否安装
		$ sudo /usr/bin/svnversion --version  #已经安装就返回具体的版本号，没有安装就会返回错误信息
	2. 如果没有安装就使用命令安装
		$ sudo apt-get install subversion
	3.安装完成后创建一个存放仓库的文件夹（一般在/home/parasaga或者/root目录下创建）
		$ sudo mkdir SvnRepo
		$ sudo cd SvnRepo
	4. 创建一个新的仓库
		$ sudo svnadmin create /root/svnRepo/usercase
	5. 配置所有匿名用户都可以提交（没有需要可以不配）
		$ sudo cd //root/svnRepo/usercase/conf
		$ sudo vim svnserve.conf
	6. 修改 anon-access = none 的none为write
	
~~~

###     权限配置
#### 		添加用户和授权

~~~Bash
    添加用户：
        $ sudo vim /root/svn/usercase/conf/passwd.conf
        在文件末尾添加：用户名=密码
    修改权限：
        $ sudo vim /root/svn/usercase/conf/authz.conf
        [groups]
        Admin:这个组的用户有读写权限
        User:这个组的用户只有读的权限

~~~
## SVN访问
~~~Text
	客户端：TortoiseSVN
	访问路径：svn://ip/仓库名称
	例如：svn://192.168.1.98/usercase/
~~~
#### 		参考文档

​		[SVN权限配置](https://www.cnblogs.com/fps2tao/p/8672746.html)
​		[SVN常用命令](https://www.cnblogs.com/chy-op/p/10230273.html)

## SVN 备份

~~~Text
	使用FZ直接拷贝仓库到本地即可
~~~

## SVN 还原
~~~Bash
    1. 把备份的仓库拷贝到服务器上直接覆盖原来的文件
    2. 重启SVN
        $ sudo Killall svnerve  //停止
        $ sudo Svnserve –d –r /root/SvnRepo  //启动

~~~

