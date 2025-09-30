import numpy as np
"""
This script demonstrates basic NumPy array operations and manipulations.

The code showcases:
- Basic array creation and multiplication
- Multidimensional array creation and indexing
- Array slicing operations on 2D arrays

The line 'print(array_2d[0:,1:4:2])' performs the following:
- 0: selects all rows (due to empty value before colon)
- 1:4: selects columns from index 1 (inclusive) to 4 (exclusive)
- :2 indicates a step of 2 (taking every second column in the range)
This effectively extracts columns 1 and 3 from all rows of the array.

Returns:
    Prints a slice of the 2D array containing all rows but only columns 1 and 3
    (using 0-based indexing)
"""


array = np.array([1, 2 , 3, 4 ,5])
array = array * 2
# print(array.ndim) # checks the multidimensions

# print(array.shape)#checks the shape of the array showing length, 

array_two = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                      [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                      [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

# MULTIDIMENSIONAL ARRAY indexing
number_sum = array_two[0,1,1] + array_two[2,2,2]
# print(number_sum)

# SLICING
# 2d array
array_2d = np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]])
# array[start:stop:step]
# print(array_2d[-1::-1])

#column selection

# print(array_2d[0:,1::-1])

# row and column selection
# print(array_2d[0:3, 1:4])

# Scalar arithmetic
array = np.array([1, 2,3])

# print(array + 1)  # adds 1 to each element
# print(array * 2)  # multiplies each element by 2
# print(array / 2)  # divides each element by 2
# print(array - 1)  # subtracts 1 from each element

# vector arithmetic
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# print(np.pi * array1 **2)
# print (array1 + array2)
# print(array1 - array2)
# print(array1 * array2)

# comparison

scores = np.array([85, 90, 78, 92, 88])
# print (scores >= 90)  # returns a boolean array indicating which scores are >= 90

scores[scores >= 90] = 100  # sets scores >= 90 to 100\
# print(scores)

# broadcasting
array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[10], [20], [30], [40]])

# print(array1.shape)
# print(array2.shape)

# print(array1*array2)

# aggreagation functions
array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(np.sum(array, axis=0))  # sum of each column
# print(np.sum(array, axis=1))  # sum of each row
# print(np.sum(array))         # sum of all elements
# print(np.mean(array))        # mean of all elements
# print(np.std(array))         # standard deviation of all elements
# print(np.var(array))         # variance of all elements
# print(np.min(array))         # minimum element
# print(np.max(array))         # maximum element
# print(np.argmin(array))      # index of minimum element
# print(np.argmax(array))      # index of maximum element

# filtering
ages = np.array([[22, 25, 3, 35, 4, 45, 50, 65], [39, 22, 25 ,99, 18, 19, 20, 21]])
teenagers = ages[ages < 20]
# adults = ages[(ages >= 20) & (ages < 65)]
print(teenagers)
# print(adults)

adults = np.where(ages >=18, ages, 0)
print(adults)

#random number
rng = np.random.default_rng(seed=1)  # create a random number generator 
print(rng.integers(1,7, size=(3,3)))  # generate a 3x3 array of random integers between 1 and 6 (inclusive of 1, exclusive of 7)

#floating point
print(np.random.uniform(low=-1, high=1, size=(3,2)))

#shuffle
rng= np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)    

# random choice
fruits = np.array(['apple', 'banana', 'cherry', 'date'])
fruits = rng.choice(fruits, size=2 )
print(fruits)