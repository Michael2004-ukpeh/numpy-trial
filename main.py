import numpy as np
print(np.__version__)

array = np.array([1, 2 , 3, 4 ,5])
array = array * 2
print(array.ndim) # checks the multidimensions

print(array.shape)#checks the shape of the array showing length, 

array_two = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                      [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                      [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

# MULTIDIMENSIONAL ARRAY indexing
number_sum = array_two[0,1,1] + array_two[2,2,2]
print(number_sum)

# SLICING
# 2d array
array_2d = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15]])
# array[start:stop:step]
# print(array_2d[-1::-1])
