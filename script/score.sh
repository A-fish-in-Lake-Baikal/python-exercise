
#! /bin/zsh
echo -n "plese input a score:"
read SCORE
if [ "$SCORE" -lt 60 ]; then
	echo -e "\e[1;32m你的成绩等级为C"

elif [ "$SCORE" -lt 80 -a "$SCORE" -ge 60 ]; then
	 echo -e "\e[1;33m你的成绩等级为B"

elif [ "$SCORE" -ge 80 ]; then
        echo -e "\e[1;34m你的成绩等级为A"
fi 

