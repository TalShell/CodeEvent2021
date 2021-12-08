import math
import numpy as np 
import time

# Let's define the series xi(n) which represent how many fish with i cycle left in day n
# xi verifies these equations
# x_i(n+1) = x_{i+1}(n) ( fish of previous got their cycle reduced by one hence )
# this holds for i in { 0,1,2,3,4,5,7}
# but for i = 6, these creature can come from two different flows:
#  - either the parent whose cycle =0 got a new born and his cycle became 6
#  - or it comes from those child whos cycle was =7 in previous day
# then x6(n+1) = x0(n) + x7(n)
# x8(n+1) = x0(n) its the number of new born fishes which is the number of parent whos cycle was =0 in previous day.
# all this get translated into this nice looking matricial product:
# X(n+1) = M.dot(X(n))
M = np.array([
     [0,1,0,0,0,0,0,0,0],  #0
     [0,0,1,0,0,0,0,0,0],  #1
     [0,0,0,1,0,0,0,0,0],  #2
     [0,0,0,0,1,0,0,0,0],  #3
     [0,0,0,0,0,1,0,0,0],  #4
     [0,0,0,0,0,0,1,0,0],  #5
     [1,0,0,0,0,0,0,1,0],  #6
     [0,0,0,0,0,0,0,0,1],  #7
     [1,0,0,0,0,0,0,0,0]   #8
    ])


def get_population_at_date(N,start_population):
	while N > 0:
		start_population = np.dot(M,start_population)
		N -=1
	print(start_population.sum())

def get_data():
	path = str(input())
	nb_fish =[]
	N = 256
	t0 = time.time()
	print("Days {} ",N)
	with open(path) as file:
		start_state = [x.strip().split(',') for x in file.readlines()][0]
		start_state = [int(x) for x in start_state]
		occurences={}
		start_population = []
		for i in start_state:
			if i not in occurences:
				occurences.update({i:1})
			else:
				occurences.update({i:(occurences[i]+1)})
		for i in range(9):
			if i in occurences:
				start_population.append(occurences[i])
			else:
				start_population.append(0)

		print(start_population)
		get_population_at_date(N, np.array(start_population))
		t1 = time.time()
		print("it took {}".format(t1-t0))

if __name__=="__main__":
	get_data()
