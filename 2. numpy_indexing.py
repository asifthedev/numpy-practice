import numpy as np

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

metrix = np.array(nums)

# how to access a single element
nine = metrix[2, 2]

# create a sub array with [[5 6], [8, 9]]
sub_array = metrix[1:3, 1:3]

# is change in subarray reflect in main array? 
# Answer: Yes
sub_array[0, 0] = 60
# print(metrix)

# I don't want to relect change is sub-array in main array
new_sub_array = np.array(metrix[1:3, 1:3], copy=True)
new_sub_array[0, 0] = 90
# print(metrix)
