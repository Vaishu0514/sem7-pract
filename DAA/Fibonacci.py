n = int(input("Enter the limit: "))
z=n
a = 0
b = 1
print(a,b,end = " ")
for i in range(0,n):
	c = a+b
	print(c, end=" ")
	a=b
	b=c
print()

def recur_fibo(n):
	if n <= 1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n-2))
		
print(recur_fibo(z))
