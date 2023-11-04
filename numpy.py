import numpy as np

# Python data types
# strings - represents text data 'ab'
# integer - represents integer numbers 1, 5, -4 
# float - represents real numbers 1.2, 4.5
# boolean - represents truthiness true, false
# complex - represents complex numbers 1.3+0.1j

# NumPy data types
# i - integer
# u - unsigned integer 
# b - boolean
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type (void)

print("------------------------------------------ARRAYS----------------------------------------------------")

# 0-D arrays
arr0 = np.array(12)
print(arr0)
print(arr0.ndim)

# 1-D arrays -> An array that has 0-D elements
arr1 = np.array([2,3,4,5,6,2,7,3])
print(arr1)
print(arr1.ndim)

# 2-D arrays -> An array that has 1-D elements
arr2 = np.array([[2,3], [4,2]])
print(arr2)
print(arr2.ndim)

# 3-D arrays -> An array that has 2-D elements
arr3 = np.array([[[2,3], [4,2]], [[2,3], [4,2]]])
print(arr3)
print(arr3.ndim)

# Creating an array while specifying the number of dimensions
arr4 = np.array([3,2,1], ndmin= 7)
print(arr4)

print("------------------------------------------INDEXING----------------------------------------------------")

# Indexing
print(arr1[2])

print("------------------------------------------ARRAY SLICING----------------------------------------------------")

# Array Slicing
# Taking elements from one given index to another given index
arr5 = np.array([4,7,2,7])
# arr[start:end:step]
print(arr5[0:3]) # Will print the current array

# Refer an element from the end using negative slicing
arr6 = np.array([4,7,2,7])
print(arr6[-2:])

print("------------------------------------------DATA TYPES----------------------------------------------------")
arr7 = np.array([[8,4,5],[8,4,5]])
print(arr7.dtype)

# Creating an array with datatype
arr8 = np.array(["Banana", "Mango"], dtype="S")
print(arr8)
print(arr8.dtype)

# Convert datatype from existing array
arr9 = np.array([-1, 3.5, 5])
arr9.astype(int)
print(arr9)

# integer to boolean
arr10 = np.array([-1, 5])
newarr10 = arr10.astype(bool)
print(newarr10)

print("------------------------------------------NumPy Array Copy vs View----------------------------------------------------")
# Copy - A new array. Owns the data. Any changes made to the copy will not affect the original array and vice versa
# View - A view of the original array. Does not own the data. Changes made to the view will affect the original array and vice versa

# Copy array
arr11 = np.array([6,4,2])
arr12 = arr11.copy()

#  make changes in original array
arr11[2] = 12

print("-------Original Array--------")
print(arr11)
print("-------Copy Array--------")
print(arr12)

# check if it owns its data
print("--Copy array check ownership--")
print(arr12.base) # None shows it owns the data
print("--End--")

# View array
arr13 = np.array([6,4,2])
arr14 = arr13.view()

# make changes to view
arr14[0] = 100

print("-------Original Array--------")
print(arr13)
print("-------View Array--------")
print(arr14)

# check if it owns its data
print("--View array check ownership--")
print(arr14.base) # Refers to the original project
print("--End--")

print("------------------------------------------Shape of Arrays---------------------------------------------------")
# The shape of an array is the number of elements in each dimension.
# shape - returns a tuple with each index having the number of corresponding elements
arr15 = np.array([[9,5], [7,3], [8,1]]) # It seems like the 1-D arrays should be of the same size
print("---Shape of array---")
print(arr15.shape)

# Reshaping arrays
# changing the shape of an array

# 1-D to 2-D
arr16 = np.array([1,2,3,4,5,6,7,8,9])
arr17 = arr16.reshape(3, 3) # the No of dimensions should divide the number of elements in the original array
print("--1-D to 2-D Reshaped Array--")
print(arr17)

# 1-D to 3-D
arr18 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr19 = arr18.reshape(3,2,2)
print("--2-D to 3-D Reshaped Array--")
print(arr19)
print(arr19.ndim)

print("------------------------------------------Array iteration---------------------------------------------------")
# Going through elements one by one

print("---Using for loop---")
arr20 = np.array([[1,2],[3,4],[8,9],[11,12]])
for element in arr20:
    for e in element:
        print(e)

print("---Using nditer---")
# nditer sorts the problem of iterating through arrays with high dimensions
# prevents usage of n for loops
arr21 = np.array([[[1,2],[3,4]],[[8,9],[11,12]]])
for element in np.nditer(arr21):
    print(element)

print("---Using ndenumerate---")
# enables mentioning sequence number of elements one by one.
arr22 = np.array([[[1,2],[3,4]],[[8,9],[11,12]]])
for index, element in np.ndenumerate(arr22):
    print(element, index)

print("------------------------------------------NumPy array joining---------------------------------------------------")
# Putting contents of 2 or more arrays in a single array
print("-----------Using concatenate--------------------")
print("-----------1-D arrays--------------------")
arr23 = np.array([1,2,3])
arr24 = np.array([4,5,6])
# Join above arrays
arr25 = np.concatenate((arr23, arr24))
print(arr25)

print("-----------2-D arrays--------------------")
arr26 = np.array([[1,2,3],[4,5,6]])
arr27 = np.array([[7,8,9],[10,11,12]])
# Join above arrays
arr28 = np.concatenate((arr26, arr27))
print(arr28)

print("-----------Using Stack--------------------")
# Done along a new axis

arr29 = np.array([1, 2, 3])

arr30 = np.array([4, 5, 6])

arr31 = np.stack((arr29, arr30), axis=0)
print(arr31)

print("-----------Stacking along Rows--------------------")
arr32 = np.array([1, 2, 3])

arr33 = np.array([4, 5, 6])

arr34 = np.hstack((arr32, arr33))
print(arr34)

print("-----------Stacking along Columns--------------------")
arr35 = np.array([1, 2, 3])

arr36 = np.array([4, 5, 6])

arr37 = np.vstack((arr35, arr36))
print(arr37)

print("-----------Stacking along Height--------------------")
arr38 = np.array([1, 2, 3])

arr39 = np.array([4, 5, 6])

arr40 = np.dstack((arr38, arr39))
print(arr40)

print("------------------------------------------NumPy array splitting---------------------------------------------------")
# Reverse operation of joining
# Divides single array into multiple arrays
arr41 = np.array([1, 2, 3, 4, 5, 6])

newarr41 = np.array_split(arr41, 4)
print(newarr41)

print("------------------------------------------NumPy array searching---------------------------------------------------")
# searching array for a certain value, and return the indexes that get a match.
arr42 = np.array([1, 2, 3, 2, 5, 2])

# equal
x = np.where(arr42 == 2)
print("--Equal--")
print(x) # Prints the indexes

# modulus
x1 = np.where(arr42 % 2 == 0)
print("--Modulus--")
print(x1)

# odd
x2 = np.where(arr42 % 2 != 0)
print("--Odd Numbers--")
print(x2)

print("--Search Sorted--")
# Search sorted
# searchsorted() - performs binary search in an array and returns an index where the specified value would be inserted, to maintain the search order
arr43 = np.array([1, 2, 5, 7, 8, 9])
x3 = np.searchsorted(arr43, 2)
print(x3)

# Searching for multiple values
print("---Searching for multiple values---")
x4 = np.searchsorted(arr43, [2,3])
print(x4)

print("------------------------------------------NumPy array sorting---------------------------------------------------")
# putting elements in an ordered sequence.
print("--sorting integers--")
arr44 = np.array([3, 2, 0, 1])
print(np.sort(arr44))

print("--sorting strings--")
arr45 = np.array(["Mango", "Banana", "Apple"])
print(np.sort(arr45))

print("--sorting booleans--")
arr46 = np.array([False, False, True, False])
print(np.sort(arr46)) # False False False True

print("--sorting 2-D array--")
arr47 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr47))

print("------------------------------------------NumPy array filter---------------------------------------------------")
# Getting some elements out of an existing array and creating a new array
# It uses boolean index list - A list of booleans corresponding to indexes in the array.
arr48 = np.array([67, 23, 56, 78])
x5 = [True, True, False, True] # Hard coded conditions
newarr48 = arr48[x5]
print("--The filtered array--")
print(newarr48)

# Creating a dynamic filter array
arr49 = np.array([67, 80, 58, 28, 23, 56, 78, 43, 15, 17])
x6 = [] # Create an empty list
for element in arr49:
    if element > 40:
        x6.append(True)
    else:
        x6.append(False)
newarr49 = arr49[x6]
print("--The filtered array using a created filter list--")
print(newarr49)

print("--Creating Filter Directly From Array--")
arr50 = np.array([67, 80, 58, 28, 23, 56, 78, 43, 15, 17])
x7 = arr50 > 50
newarr50 = arr50[x7]
print(newarr50)