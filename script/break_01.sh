#!/bin/zsh
for I in A B C D
do
	echo -n "$I:"
	for J in 'seq10'
		do
			if [$J-eq5]; then
				break
				#break2
			fi
			echo -n "$J"
		done
	echo
done
echo
