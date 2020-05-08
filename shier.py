for i in range(101,200):
	m=int(i/2)
	n=0
	for j in range(2,m):
		if i%j==0:
			n=1
	if (n!=1):
		print (i)

