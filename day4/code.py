import numpy as np 
class Board:
	def __init__(self,data,nrows,ncols,idx):
		self._idx = idx
		self._nrows = nrows
		self._ncols = ncols
		self._data = np.array(data.copy())
		self._won= False

	def get_sum(self):
		s=0
		for l in self._data:
			s +=sum(int(x) if x !='X' else 0 for x in l)
		print(s)
		return s
	def update(self,i):
		self._data = [ ['X' if x == i else x for x in l ] for l in self._data]
		bingo = ['X' for i in range(self._ncols)]
		if bingo in self._data :
			print("BINGO")
			return True
		if bingo in np.array(self._data).T.tolist():
			print("BINGO")
			return True			
		else :
			return False
        
	def __str__(self):
		data_str = ''.join(str(e) for e in self._data)
		return ("Board {} {} {} \n {} ".format(self._idx,self._nrows,self._ncols,data_str))

	def __repr__(self):
		print("Board {} {} {} ".format(self._idx,self._nrows,self._ncols))
		for i in range(self._nrows):
			data_str = ' '.join(str(e) for e in self._data[i])
			print(data_str)
		print("\n")
		return " "

def get_data():
	path = str(input())
	with open(path) as file:
		lines = [x for x in file.readlines()]
		numbers = [int(x) for x in lines[0].split(',')]
		boards=[]
		data=[]
		idx = 0
		for i in lines[1:]:
			if i == '\n' :
				if data:
					b= Board(data,len(data),len(data[0]),idx)
					boards.append(b)
					idx +=1
					data.clear()
			else:
				data.append([int(x) for x in i.strip().split()])

		print("Input nbrs: ", numbers)
		for b in boards:
			repr(b)
		return  boards,numbers,

def process(boards, numbers):
	for i in numbers:
		for b in boards:
			if not b._won and b.update(i):
				print("winner is :", b._idx)
				return i,b._idx
	return -1,-1

def process2(boards, numbers):
	last_winner =-1
	last_nbr = -1
	for i in numbers:
		for b in boards:
			if not b._won and b.update(i):
				print("winner is :", b._idx)
				b._won= True
				last_winner = b._idx
				last_nbr = i
	return last_nbr ,last_winner

def part1():
	boards,numbers = get_data()
	nb , winner = process(boards, numbers)
	if winner != -1:
		repr(boards[winner])
		print(nb * boards[winner].get_sum())

def part2():
	boards,numbers = get_data()
	last_nbr , last_winner = process2(boards, numbers)
	if last_winner != -1:
		repr(boards[last_winner])
		print(last_nbr * boards[last_winner].get_sum())

if __name__=="__main__":
	part1()
	part2()



