import numpy as np

# create
metrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Adding new row in numpy matrix
metrix = np.vstack([metrix, np.array([7, 8 , 9])])

# Add new column in metrix
metrix = np.hstack([metrix, np.array([[1], [1], [1]])])

# Appending in vector
row_vector = np.array([1, 2, 3])
row_vector = np.append(row_vector, 4)
# print(row_vector)

# Insert element at specific index
row_vector = np.insert(row_vector, 0, 1.1)

# Reshape the array but not inplace
vector = np.arange(start=1, stop=10) # 1 -> 9
vector = vector.reshape((3, 3))

# Reshape the orignal array inplace
vector.resize((9,))

# Delete an item from a vector
vector = np.delete(vector, [0])

# Delete an item from metrix
metrix = np.delete(metrix, [0])
print(metrix)

