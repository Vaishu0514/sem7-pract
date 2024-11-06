job_count = int(input("Enter the number of jobs: "))
data1 = {}
data2 = {}
for i in range (0,job_count):
	job_name = input("Enter job name: ")
	job = int(input("Enter the job: "))
	deadline = int(input("Enter the deadline: "))
	data1[job] = job_name
	data2[job] = deadline
sorted_key = sorted(data2,reverse=True)
val = list(data2.values())
maximum = max(val)
max_count = val.count(maximum)
max_limit = maximum*max_count
time = [0 for x in range(0,max_limit)]
itr = 0
for i in range(0,job_count):
	place = data2[sorted_key[itr]]-1
	if time[place] == 0:
		time[place] = data1[sorted_key[itr]]
		itr+=1
	else:
		itr+=1
print(time)
