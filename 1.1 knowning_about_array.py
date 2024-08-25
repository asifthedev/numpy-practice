import numpy as np

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

metrix = np.array(nums)

# What's the shape of the metrix?
print('shape ->', metrix.shape)

# What's the dimentions of the metrix?
print('dimension ->', metrix.ndim)

# How many items there in the metrix?
print('total items ->', metrix.size)

# What's size in bytes for each item
print('One item\'s size ->', metrix.itemsize, 'bytes')