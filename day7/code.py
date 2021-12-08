import numpy as np 
import math

# In this challenge we optimize sum Ei(optim) where Ei 
# is the requiered energy to move from xi to optimal position


# when energy cost is constant then median is the best trade-off
# we optimize sum |xi - optim| where optim covers list of crabes positions 
def needed_fuel_to_align_to_median(crabs):
	median = np.median(crabs)
	distances = np.asarray([abs(x-median) for x in crabs])
	return int(distances.sum())

# energy cost is increasing at each step: E ~ O(n**2) with n number of steps
# we optimise sum s(abs(xi-optim)) where s(i) = 1 + 2 +.. +i = i(i+1)/2
# we optimize E(x) = N/2*x**2 - 0.5 sum(2*xi-1)*x +0.5 sum (xi**2 -xi)
def needed_fuel_to_align_to_optimal(crabs):
	optimal = (crabs.sum() - 0.5*len(crabs))/len(crabs)
	# we could get fraction position, we check its neighbours 
	optimal_low =  math.floor(optimal)
	optimal_high =  math.ceil(optimal)
	optimal_low_cost = np.asarray([np.array(range(abs(x-optimal_low)+1)).sum() for x in crabs]).sum()
	optimal_high_cost = np.asarray([np.array(range(abs(x-optimal_high)+1)).sum() for x in crabs]).sum()

	return (optimal, min(optimal_low_cost,optimal_high_cost))
	


def get_data():
	path = str(input())
	with open(path) as file:
		lines = [x.strip().split(',') for x in file.readlines()]
		crabs = np.asarray([int(x) for x in lines[0]])
		#print(crabs)
		print("Case1: {}".format(needed_fuel_to_align_to_median(crabs)))
		print("Case2: {}".format(needed_fuel_to_align_to_optimal(crabs)))

if __name__=="__main__":
	get_data()
