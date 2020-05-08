for i in range(1,5):
	for j in range(1,5):
		for x in range(1,5):
			if (i!=x) and (i!=j) and (j!=x):
				print(i,j,x)
