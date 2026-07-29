import numpy as np


"""I is used to define the array """
list1=[1,2,3]
arr1=np.array(list1) 


"""It shows that this is the array class """
# print(type(arr1)) 

list2=[10,11,12]
arr2=np.array(list2)
# print(arr2)


"""Use Indexing and Slicing concept on the array."""
# print(arr2[0:2])
# print(arr1[::-1])

# print(arr1[2]) # it is used to fetch particular location element.

arr3=np.array([arr1,arr2])
# print(type(arr3))
# print(arr3)
""" array[row_slice, column_slice] """

# print(arr3[0:2,1:3])
# print("i want to print 1 row with 1 index value to last index value ",arr3[1,1:3]) # arr[row,column]
# print("i want to print 0 row with whole elements ",arr3[0,0:3])
# print("I want to print only 1 column of both rows", arr3[:,0])
# print("I want to print Oth index value of oth row and 2nd index value of 1th row :", arr3[[0,1],[0,2]]) # arr3[[rows],[columns]]---> arr3[[r1,r2,r3],[c1,c2,c3]]

# print("I want to print only 1th index row of 1th index value :",arr3[1,[1]])
# print("I want to print 0th row of 2nd column index value and 1st row of 0th column index value :", arr3[[0,1],[2,0]])

"""NOW WE PERFORM SOME MATHEMATICAL OPERATIONS """
# Addition of two arrays :
# print(f"Adding two lists: \n{list1}\n{list2}\nadditon :{list1+list2}\n")
# print(f"Addition two arrays :\n{arr1}\n{arr2}\naddition :{arr1+arr2}")

# Multipication of arrays :
# print(f"arr1 multiplied by arr2: {arr1*arr2}")

# Dividation of arrays :
# print(f"arr2 divided by arr1 : {arr2/arr1}")

# Power of arrays 
# print(f"arr2 raised to the power of arr1 : {arr2**arr1}")


"""HOW TO GENERATE ARRAYS EASILY."""
# print(f"A series of Zeros : {np.zeros(7)}") # zeros() generates the continuous zeros.
# print(f"A series of ones : {np.ones(9)}") # ones() generates the continuos ones.
# print(f"A series of number : {np.arange(1,11)}") # np.arange(start,end+1) is used to print auto series 
# print(f"Numbers spaced apart by 2 : {np.arange(2,11,2)}")
# print(f"Numbers spaced apart by float : {np.arange(0,11,2.5)}")
# print(f"Every 5th number from 30 in reverse order : {np.arange(30,-1,-5)}")
# print(f"11 linearly spaced numbers between 1 and 5 : {np.linspace(1,5,11)}") # Linspace() generates an array of evenly (linearly) spaced numbers over a specified mathematical interval.


"""Dimension, shaping, sizing and data type of the 2d array"""

# print(f"Dimension of this matrix : {arr3.ndim}") # ndim(var) gives dimension of the matrix.
# print(f"Size of this matrix: {arr3.size}") # var.size tell us how many element present in the matrix.
# print(f"Shape of this matrix: {arr3.shape}") # var.shape tell us the shape of matrix in (no_row,no_column)
# print(f"Data type of this matrix : {arr3.dtype}") # dtype tell us the data type of the matrix 


"""Multi-dimensional array"""
list3=[21,22,23]
arr4=np.array([list1,list2,list3])
# print(arr4)
# print(type(arr4))

"""Zeros, Ones, Random and Identity Matrics and Vactors"""
# print(f"vector of zeros : {np.zeros(5)}")
# print(f"matrix of Zeros : {np.zeros((3,4))}") # zeros((rows, columns))
# print(f"Vector of ones : {np.ones(5)}")
# print(f"Matrix of Ones : {np.ones((4,5))}") # ones((rows, columns))
# print(f"Identity martix of dimension 2: {np.eye(2)}") # np.eye() gives an identity matrix.
# print(f"Identity matrix of dimension 4: {np.eye(4)}")
# print(f"random matrix of shape (4,4) \n{np.random.randint(low=1,high=100,size=(4,4))}")
# if we use np.random.randint(low=0,high=10,size=(4,3))

"""Reshaping, Ravel, Min, Max, Sorting"""
# a=np.random.randint(1,100,30)
# b=a.reshape(2,3,5) # reshape(matrix, rows , column) changes the shape of an array without altering its underlying data.
# c=a.reshape(6,5) # here reshape(row, column)
# print(f"Shape of a: {a}")
# print(f"Shape of b: {b}")
# print(f"Shape of c: {c}")

"""Conditional Subsetting"""
mat=np.random.randint(10,100,15).reshape(3,5)
print(f"Matrix of random 2-digit number \n {mat}")
print(f"Elements greater than 50 \n {mat[mat>50]}")

# we can also use for find the boolean value according to our needs 
print(mat>50)
# after finding the boolean value then we use according to needs.
print(mat*(mat>50))

