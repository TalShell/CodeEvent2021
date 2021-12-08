
def compute(lines,L):
	tosum=[]
	for i in range(0,len(lines)-L+1):
		tosum.append(sum(lines[i:i+L]))

	pos = 0
	for i in range(len(tosum)-1):
		if tosum[i+1] > tosum[i]:
			pos +=1
	return pos

def gold1():
	path = str(input())
	with open(path) as file:
		lines = [int(x.strip()) for x in file.readlines()]
		print(compute(lines,1))

def gold2():
	path = str(input())
	with open(path) as file:
		lines = [int(x.strip()) for x in file.readlines()]
		print(compute(lines,3))

if __name__=="__main__":
	gold1()
	gold2()
