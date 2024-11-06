def optCost(freq, i, j): 
	if j < i:    
		return 0
	if j == i:     
		return freq[i] 
	fsum = Sum(freq, i, j) 
	Min = 999999999999
	for r in range(i, j + 1):
		cost = (optCost(freq, i, r - 1) + optCost(freq, r + 1, j)) 
		if cost < Min: 
			Min = cost
	return Min + fsum
def optimalSearchTree(keys, freq, n):
	return optCost(freq, 0, n - 1)
def Sum(freq, i, j):
	s = 0
	for k in range(i, j + 1):
		s += freq[k] 
	return s
k = int(input("Enter the number of keys keys: "))
keys = [] 
freq = [] 
for i in range(0,k):
	key = int(input("Enter key: "))
	val = int(input("Enter frequency: "))
	keys.append(key)
	freq.append(val)
print("Cost of OBST is", optimalSearchTree(keys, freq, k))
