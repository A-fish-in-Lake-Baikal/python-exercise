# Redmine安装维护
## 服务器说明：
~~~Text
  Ubuntu版本：18.04.3
  机器名称：Redmine
  机器IP：192.168.1.98
  机器所在服务器：19.2.168.1.168
  用户名：root
  密码：Test12#$%198
  MySQL版本：Ver 14.14 Distrib 5.7.31
  Redmine版本：3.4.6.stable（根据官方文档安装的就是这个版本）
  Redmine备份文件路径：/backup/redmine（后缀是tgz)
~~~

### 一、安装

#### 1.1根据官方文档安装：
   [官方文档](https://www.redmine.org/projects/redmine/wiki/HowTo_Install_Redmine_on_Ubuntu_step_by_step )

~~~bash
	1. 安装Apache和相关插件
    	$ sudo apt-get install apache2 libapache2-mod-passenger
    2. 安装MySQL
    	$ sudo apt-get install mysql-server mysql-client
    3. 安装Redmie
    	$ sudo apt-get install redmine redmine-mysql
    4. 安装过程中先选择MySQL数据库，然后再指定redmine的密码和确认密码
    5. 安装所需插件，先确保已经安装gem
        $ sudo gem update
        $ sudo gem install bundler
	6. 配置Apache
    	6.1 在配置文件中添加一行PassengerDefaultUser www-data,如下图：
    	$ sudo vim /etc/apache2/mods-available/passenger.conf
~~~

![Apache配置文件1](https://i.loli.net/2020/08/17/DQ7SZMrlUFCviPV.png)

~~~xml
	7. 修改文件/etc/apache2/sites-available/000-default.conf，复制以下内容直接覆盖
        <VirtualHost *:80>
            # The ServerName directive sets the request scheme, hostname and port that
            # the server uses to identify itself. This is used when creating
            # redirection URLs. In the context of virtual hosts, the ServerName
            # specifies what hostname must appear in the request's Host: header to
            # match this virtual host. For the default virtual host (this file) this
            # value is not decisive as it is used as a last resort host regardless.
            # However, you must set it for any further virtual host explicitly.
            #ServerName www.example.com

            ServerAdmin webmaster@localhost
            DocumentRoot /var/www/html/redmine

            # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
            # error, crit, alert, emerg.
            # It is also possible to configure the loglevel for particular
            # modules, e.g.
            #LogLevel info ssl:warn
            PassengerAppRoot /usr/share/redmine
            ErrorLog ${APACHE_LOG_DIR}/error.log
            CustomLog ${APACHE_LOG_DIR}/access.log combined

            # For most configuration files from conf-available/, which are
            # enabled or disabled at a global level, it is possible to
            # include a line for only one particular virtual host. For example the
            # following line enables the CGI configuration for this host only
            # after it has been globally disabled with "a2disconf".
            #Include conf-available/serve-cgi-bin.conf
		</VirtualHost>
		# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
~~~
~~~bash
	8. 创建符号链接
		$ sudo ln -s /usr/share/redmine/public/ /var/www/html/
~~~
~~~bash
	9. 创建并设置Gemfile.lock文件的所有权，以便apache的www-data用户可以访问它：
		$ sudo touch /usr/share/redmine/Gemfile.lock
		$ sudo chown www-data:www-data /usr/share/redmine/Gemfile.lock
	10. 重启整个机器
		$ sudo reboot
	11. 访问Redmie
		例如：http://127.0.0.1/redmine
~~~

#### 1.2报错信息处理
~~~bash
	1.500错误，重启Apache服务
		$ sudo service apache2 restart
	2.其他错误页面，自行百度解决或者重启服务
		$ sudo reboot
~~~

### 二、备份
~~~Bash
	2.1 将文件夹内的备份脚本上传到redmine服务器/backup/redmine路径下，没有该路径就先创建
	2.2 创建定时任务
		$ sudo crontab -e    #第一次进入需要选择编辑器，直接选择vi就行，然后在文件末尾加入以下两行
		0 0 * * 2,4,6 /backup/redmine/backupredmine.sh
		0 6 * * * /backup/redmine/apache2_restart.sh >> /backup/redmine/test.log 2>&1
	2.3 保存并退出
~~~

### 三、还原

####   3.1 环境本身未损坏，可以使用备份文件还原

~~~bash
	3.1.1 把备份的压缩文件拷贝到服务器redmine的安装目录下
	3.1.2 解压备份文件
		$ sudo tar zxvf 备份文件.tgz
	3.1.3 把解压后的files文件夹的内容拷贝到redmine的安装目录，gemfile和gemfile.lock不用拷贝
	3.1.4 还原数据库
		$ sudo mysql -u用户名 –p密码 数据库名 < sql备份文件路径/文件名
		例如：mysql -u root -p redmine < redmine.db.bak
	3.1.5 重启MySQL和Apache服务
		$ sudo systemctl restart mysql
		$ sudo service apache2 restart
~~~

#### 3.2 环境已经损坏无法登录
~~~Text
	3.2.1 旧环境关机，把备份好的虚拟机文件上传到服务器
	3.2.2 恢复虚拟机
	3.2.3 参照步骤2.1进行后续恢复步骤
~~~
