import numpy as np
import time
#creating anarrayu
# arr = np.arange(5)



# #creating an array
# a1 = np.array([2,4,6,7])
# print(a1)


# #comparing the times of operations

a1 = np.arange(10000000)
a2 = np.arange(10000000)

start = time.time()

x3 = a1 + a2

print(" tiume taken is ", time.time()- start)
