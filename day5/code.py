import numpy as np

class Point():
	def __init__(self,x,y):
		self._x = x 
		self._y = y
	def __repr__(self):
		return '{} {}'.format(self._x,self._y)
def line(x,y,z,t):
    a = (y-t)/(x-z)
    b = y -a*x 
    return a,b

def valid(start, end, diagonal=False):
	print(start,end)
	points = []
	if start[0] == end[0]:
		for i in range(min(start[1],end[1]),max(start[1],end[1])+1):
			points.append(Point(start[0],i))
		return points
	if start[1] ==end[1]:
		for i in range(min(start[0],end[0]),max(start[0],end[0])+1):
			points.append(Point(i,start[1]))
		return points
	if diagonal and start[0] != end[0] and start[1] !=end[1]  :
		a,b = line(start[0],start[1],end[0],end[1])
		# Y =a*X +b
		print(a,b)
		for x in range(min(start[0],end[0]),max(start[0],end[0])+1):
			for y in  range(min(start[1],end[1]),max(start[1],end[1])+1):
				if y == a*x+b:
					print(" x {} y {} a*x+b {} ".format(x,y,a*x+b))
					points.append(Point(x,y))
		return points
	else:
		return None

def get_secure_spots(lines, diagonal=False):
	matrix = np.zeros((1000,1000))
	for l in lines:
		start = [int(x) for x in l[0].split(',')]
		end = [int(x) for x in l[1].split(',')]
		points = valid(start,end,diagonal)
		print(points)
		if points:
			for pt in points:
				matrix[pt._x][pt._y]+=1

	print(matrix)
	print((matrix>1).sum())

def get_data(diagonal =False):
	path = str(input())
	with open(path) as file:
		lines = [x.split('->') for x in file.readlines()]
		lines =[ [x.replace("\n","") for x in l]for l in lines]
		print(lines)
		get_secure_spots(lines,diagonal)




if __name__=="__main__":
	get_data()
	get_data(True)



