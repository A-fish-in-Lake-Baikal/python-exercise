def mysum(l):
	print(l)
	if not l:
		return 0
	else:
		print(mysum(l[:-1]))
		# return l[0]+mysum(l[1:])


if __name__=='__main__':
	mysum([1,2,3,4,5,6,7])