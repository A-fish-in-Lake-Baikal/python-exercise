#! /usr /bin/expect

set ip [lindex $argv 0]
set user [lindex $argv 1]
set passwd 00000
set timeout 5

spawn ssh $user@$ip

expect {
	"yes/no" { send "yes\r"; exp_continue }
	"password:" { send "$passwd\r" };
}
#interact
expect "+_"
send "成功"
expect eof
