itr = int(input("Enter the number of iteration: "))
W = {}
ratio = []
for i in range(0,itr):
	w = int(input("Enter the weight: "))
	p = int(input("Enter the profit: "))
	W[w] = p
	ratio.append(p/w)
y = list(W)
z = [x for _,x in sorted(zip(ratio,y),reverse=True)]
print(z)
C = int(input("Enter the capacity: "))
P = 0
for i in range(0,itr):
	if(C<=0):
		break
	elif(C>0 and z[i]<=C):
		C = C-z[i]
		P = P+W[z[i]]
	elif(C>0 and y[i]>C):
		P = P + (W[z[i]]*(C/z[i]))
		C = 0
print(P)