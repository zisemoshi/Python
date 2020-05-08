salary=int(input("please your money :"))
arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for i in range(0,6):
	if salary>arr[i]:
		r+=(salary-arr[i])*rat[i]
		print("({}-{})*{}={}".format(salary,arr[i],rat[i],(salary-arr[i])*rat[i]))
		salary=arr[i]
print(r)
