
def process(l,x,depth):
	if l[0] == 'forward':
		x += int(l[1])
	elif l[0] == 'down':
		depth += int(l[1])
	else:
		depth -= int(l[1])
	return x,depth

def process2(l,x,depth,aim):
	if l[0] == 'forward':
		x += int(l[1])
		depth += aim * int(l[1])
	elif l[0] == 'down':
		aim += int(l[1])
	elif l[0]=='up':
		aim -= int(l[1])
	print(x,depth,aim)
	return x,depth,aim

def compute():
	path = str(input())
	x = 0 
	depth = 0
	with open(path) as file:
		lines = [x.strip().split() for x in file.readlines()]
		for i in lines:
			x,depth = process(i,x,depth)

	print(x*depth)

def compute2():
	path = str(input())
	x = 0 
	depth = 0
	aim = 0
	with open(path) as file:
		lines = [x.strip().split() for x in file.readlines()]
		for i in lines:
			x,depth,aim = process2(i,x,depth,aim)

	print(x*depth)


if __name__=="__main__":
	compute2()

