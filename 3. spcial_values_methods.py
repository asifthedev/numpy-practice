import numpy as np

# Generate values from 1 to 10
one_to_ten = np.arange(start=1, stop=11)

# Generate values btw 1-10, create fours equal distributions
equal_dist = np.linspace(start=1, stop=10, num=4, dtype=np.int16)

# Create an filled with our own value 3
fill_with_3 = np.full(shape=(2, 3), fill_value=3)

# create an empty array of dimension (3, 3)
empty_array = np.empty(shape=(3, 3))

# Create an array filled with zeros
filled_with_0 = np.zeros(shape=(3,3))

# Create an array filled with ones
filled_with_1s = np.ones(shape=(2,2))
print(filled_with_1s)
