import numpy as np
import numpy.ma as ma

#Most locations have four adjacent locations (up, down, left, and right); locations on the edge 
#or corner of the map have three or two adjacent locations, respectively. 
#(Diagonal locations do not count as adjacent.)

# Rotate the matrix left  right up and down, a minimal point 
# will always be lower than its neighbours
# we add the safety bell around the matrix as at certain moment 
# we will compare first and last row/cols which doesn not make sense,
# hence we put max values of the the matrix around to be safe
# and we ignore it later.
def local_minima(matrix):
    return ((matrix <= np.roll(matrix,  1, 0)) &
            (matrix <= np.roll(matrix, -1, 0)) &
            (matrix <= np.roll(matrix,  1, 1)) &
            (matrix <= np.roll(matrix, -1, 1)))

# Get only local minima
# hide others
def get_minimal_cells(matrix):
    M= np.max(matrix)
    grid = np.c_[ M*np.ones(len(matrix)) , matrix, M*np.ones(len(matrix)) ]
    grid=np.r_[[grid[0]] ,grid, [grid[-1]] ]
    local = local_minima(grid)
    return matrix[~ma.masked_array(grid, mask=~local)[1:-1, 1:-1].mask]

#compute requested score
def get_score(matrix):
    local_minimal_values = get_minimal_cells(matrix)
    print(local_minimal_values)
    data = ma.masked_where(local_minimal_values == np.max(matrix), local_minimal_values)
    c = local_minimal_values[~data.mask]
    # Dirty , if previous code find a max it created a [[np.ndarray]] otherwise it keeps it 
    # as a np.ndarray
    if type(c[0]) is np.ndarray:
    	return c[0].sum()+len(c[0])
    return c.sum()+len(c)



def get_data():
	path = str(input())
	with open(path) as file:
		lines = [list(map(int,x.strip())) for x in file.readlines()]
		grid = np.asarray(lines)
		# Part 1
		print(get_score(grid))


if __name__=="__main__":
	get_data()
