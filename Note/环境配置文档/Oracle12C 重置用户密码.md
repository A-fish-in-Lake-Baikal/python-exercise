# Oracle12C 重置用户密码
## 普通用户密码忘记:
~~~cmd
	开始--> 运行--> 输入cmd 确定
	-->输入SQLPLUS / AS SYSDBA 回车
	-->alter user 用户名 identified by 密码;
	注意分号
~~~
## sys密码忘记:
~~~CMD
	找到pwdorcl.ora文件(根据自己的找到,我的在D:\Oracle12c\product\12.1.0\dbhome_1\database)-->然后删除
	开始--> 运行--> 输入cmd 确定 -->d:
	-->cd D:\Oracle12c\product\12.1.0\dbhome_1\database
	-->orapwd D:\Oracle12c\product\12.1.0\dbhome_1\database\pwdorcl.ora password=密码 entries=10;
	如果有同名文件记得先备份或删除
~~~
