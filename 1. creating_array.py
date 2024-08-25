import numpy as np
ages = [10, 20, 30]

# creating numpy array
arr = np.array(object=ages)

# define data type for items
arr = np.array(object=ages, dtype=np.int64)

# define dimension for new array
arr = np.array(object=ages, ndmin=2)