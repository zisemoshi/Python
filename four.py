year=int(input("year:"))
month=int(input("month:"))
today=int(input("today:"))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0<month<=12:
	sum=months[month-1]
else:
	print("error")
if year%400==0 or (year%4==0 and year%100!=0):
	if month>2:
		sum+=1
print(sum+today)
