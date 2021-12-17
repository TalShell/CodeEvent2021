import numpy as np
from itertools import product
import collections

#Thanks to stackoverflow, the naive approach is ugly
def neighbours(cell,size):
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c

def update_neighbours(matrix,status=[]):
    (r,c)=np.shape(matrix)
    for i,j in product(range(r), range(c)):
        if status[i][j] ==1:
            ng  = list(neighbours((i,j),r))
            status[i][j] +=1
            for it in ng:
                if  status[it]==0:
                    matrix[it] = min(10,matrix[it]+1)
                    if matrix[it] %10 == 0:
                        status[it] =1
                        # update its neighbour's neighbours...
                        update_neighbours(matrix,status)
    return matrix

#flash flash flash until it's all zeros
def simultaneous_flash(matrix):
    (r,c)=np.shape(matrix)
    count = 0
    while not np.all(matrix==0):
        matrix = matrix_update(matrix)
        count +=1
    print(count)

def matrix_update(matrix):
    matrix =matrix + 1
    status=np.logical_and((matrix%10 ==0) , (matrix>0)).astype(int)
    matrix = update_neighbours(matrix,status)

    matrix = matrix %10
    return matrix

def life_cycle(matrix,N):
    nb_flashes = 0
    while N >0:
        matrix = matrix_update(matrix)
        nb_flashes +=len(matrix[matrix ==0])
        N-=1
        print(matrix)
    print("nbflashes {}".format(nb_flashes))

def get_data():
    path = str(input())
    cycle = 100
    with open(path) as file:
        lines = [list(map(int,x.strip())) for x in file.readlines()]
        grid = np.asarray(lines)
        print(grid)
        life_cycle(grid,cycle)
        simultaneous_flash(grid)

if __name__=="__main__":
	get_data()
