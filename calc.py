#calculator
print('\t\t calculator')
print('--------------------')
a=0
b=0
choice="y"

while choice=="y":
	a=int(input("enter a 1st num"))
	b=int(input("enter a 2nd num"))
	ops=input("+,/,-,*")

	if ops=="+":
		result=a+b
	elif ops=="-":
		result=a-b
	elif ops=="/":
		result=a/b
	else:
		result=a*b

	print(result) 
	choice=input("choose (y/n)")

##rearrange the array
##find prime num betn 1-100

