import numpy as np


arr = np.array([1,2,3,4,5])

for idx , x in np.ndenumerate(arr):
    print(idx , x)


a1 = np.array([1,2,3,4])  
a2 = np.array([5,6,7,8]) 

print(np.concatenate((a1,a2)))


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)