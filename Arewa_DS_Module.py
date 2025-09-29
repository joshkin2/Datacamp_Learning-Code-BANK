# Creating Arrays
print(f"using np.array: {np.array([1, 2, 3])}")
print(f"Initiating using np.zeros: {np.zeros((2, 3))}")
print(f"using np.ones: {np.ones(5)}")
print(f"Initiating an identity matrix: {np.eye(3)}")
print(f"using np.arange: {np.arange(0, 10, 2)}")
print(f"using np.linspace: {np.linspace(0, 1, 5)}")

# Array Attributes
x = np.array([[1, 2], [3, 4]])
print(x.shape)      
print(x.ndim)       
print(x.dtype)     

# Vectorized Operations
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)
print(x * y)
print(x ** 2)

# Broadcasting
x = np.array([[1], [2], [3]])
y = np.array([10, 20, 30])
print(x + y)

# Indexing and Slicing
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x[0, 1])  
print(x[:, 1]) 
print(x[1, :])  

# Boolean Indexing
x = np.array([1, 2, 3, 4, 5])
print(x[x > 2])

# Aggregations
x = np.array([[1, 2], [3, 4]])
print(x.sum())
print(x.mean())
print(x.max(axis=0))

# Linear Algebra
x = np.array([[1, 2], [3, 4]])
y = np.linalg.inv(x)
print(y)
print(np.dot(x, y))

# Random Numbers
np.random.seed(0)
print(np.random.rand(3))
print(np.random.randn(2, 2))
print(np.random.randint(0, 10, size=5))








