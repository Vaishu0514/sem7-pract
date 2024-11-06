itr = int(input("Enter the number of objects to be inserted: "))
C = int(input("Enter the capacity of the sack: "))
W = {}
for i in range(0,itr):
	w = int(input("Enter the weight: "))
	p = int(input("Enter the profit: "))
	W[w] = p
matrix = []
z = list(W)
for i in range (0,itr+1):
	d = []
	for j in range (0,C+1):
		if(i==0 or j==0):
			d.append(0)
		elif(z[i-1]<=j):
			k1 = W[z[i-1]] + matrix[i-1][j-z[i-1]]
			k2 = matrix[i-1][j]
			if k1>k2:
				d.append(k1)
			else:
				d.append(k2)
		else:
			k = matrix[i-1][j]
			d.append(k)
	matrix.append(d)
print(matrix[itr][C])
