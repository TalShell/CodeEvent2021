
def most_common_bit(lines):
	return [int(sum(row[i] for row in lines)/len(lines)+0.5)for i in range(len(lines[0]))]

def least_common_bit(lines):
	return [round(1-sum(row[i] for row in lines)/len(lines))for i in range(len(lines[0]))]

def get_decimal(binary):
	dec = sum(t*2**(len(binary)-i-1) for i,t in enumerate(binary))
	return dec

def get_oxygen(lines,t=0):
	if len(lines) == 1:
		print(lines[0])
		return get_decimal(lines[0])
	mst=most_common_bit(lines)
	most_frequent=[]
	new_list=[]
	for i in lines:
		if i[t] == mst[t]:
			new_list.append(i)
	return get_oxygen(new_list,t+1)
	 
def get_co2(lines,t=0):
	if len(lines) == 1:
		print(lines[0])
		return get_decimal(lines[0])
	mst=least_common_bit(lines)
	most_frequent=[]
	new_list=[]
	for i in lines:
		if i[t] == mst[t]:
			new_list.append(i)
	return get_co2(new_list,t+1)

def compute():
	path = str(input())
	x = 0 
	depth = 0
	with open(path) as file:
		lines = [[int(t) for t in x.strip()] for x in file.readlines()]
		gama_code = most_common_bit(lines)
		epsilon = least_common_bit(lines)
	#print(gama_code,epsilon)
	gama = get_decimal(gama_code)
	eps = get_decimal(epsilon)
	print(gama,eps)
	print(gama*eps )

def compute2():
	path = str(input())
	x = 0 
	depth = 0
	with open(path) as file:
		lines = [[int(t) for t in x.strip()] for x in file.readlines()]
		oxy = get_oxygen(lines)
		co2= get_co2(lines)
		print(oxy*co2)
if __name__=="__main__":
	compute()
	compute2()

