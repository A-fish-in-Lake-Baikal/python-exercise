#! /usr /bin/expect

set ip 192.168.11.27
set user mawc
set passwd 00000
set timeout 5

spawn ssh $user@$ip

expect {
	"yes/no" { send "yes\r"; exp_continue }
	"password:" { send "$passwd\r" };
}
interact
