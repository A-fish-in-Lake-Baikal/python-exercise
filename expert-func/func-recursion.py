def mysum(l):
	print(l)
	if not l:
		return 0
	else:
		print(mysum(l[:-1]))
		# return l[0]+mysum(l[1:])

mysum([1,2,3,4,5])