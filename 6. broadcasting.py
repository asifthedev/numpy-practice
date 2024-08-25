import numpy as np

# Scaler broadcasting
arr1 = np.array([1, 2])
arr2 = np.array([2]) # broacasted to [2, 2]
arr1*arr2 # output: [2, 4]

# (1, 3) * (3, 1) or (3, 1) * (1, 3)  
a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([
    [1, 2, 3]
])
 
# print(a+b)

c = np.array([
    [1],
    [3]
])

d = np.array([
    [1, 2],
    [3, 4]
])

print(c*d)

