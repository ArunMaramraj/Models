import numpy as np


# a = np.array([[1,2,3], [2,3,4], [4,5,6]])

# print(a[1][2])
# print(a.shape)
# print(a.size)


a = np.array([[1,2,3], [2,3,4], [4,5,6]])
print(a)

arr = np.ones((4,4))
# print(arr)



arr1 = np.arange(1,4)
# print(arr1)


print(a.sum(axis = 0 ))
print(a.sum(axis = 1))
print(np.sqrt(a))
print(a[0:2 , 1:3] )