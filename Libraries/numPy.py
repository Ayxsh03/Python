import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a.shape) # shape of the array
print(a.dtype) # data type
print(a.size) # number of elements

print(a[2,0]) # access element
a[2,0]=5
print(a[2,:]) # access row

b= a * np.array([2,2,2])
print(b) 

#Array vs List

li = [1,2,3,4,5]
li.append(6)
print(li)

li=li*2
print(li)

arr = np.array([1,2,3,4,5]);
# arr.append(6) # AttributeError: 'numpy.ndarray' object has no attribute 'append'
arr = np.append(arr,6)
print(arr)

arr=arr+np.array([1,1,1,1,1,1])
print(arr)

arr=arr**2
print(arr)

# Dot product
dot=0
for i in range(len(arr)):
    dot+=arr[i]*arr[i]
print(dot)

dot1 = np.dot(li,li)
print(dot1)

dot2 = np.dot(arr,arr)
print(dot2)

# Matrix multiplication
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.dot(a,b))

# Matrix transpose
print(a.T)

# Matrix inverse
c=np.linalg.inv(a)
print(c)

# Matrix determinant
d=np.linalg.det(a)
print(d)

# Matrix diagonal
print(np.diag(a))

# Matrix trace
print(np.trace(a))

# Eigen values and Eigen vectors
eig=np.linalg.eig(a)
print(eig)

# Solving linear equations
# 2x+3y=8
# 3x+4y=18
a=np.array([[2,3],[3,4]])
b=np.array([8,18])
print(np.linalg.solve(a,b))
print(np.linalg.inv(a).dot(b))

# Generating random numbers
print(np.random.rand(3,3))  # uniform distribution
print(np.random.randn(3,3)) # normal distribution
print(np.random.randint(1,10,3)) # random integers

# Reshaping
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.reshape(1,9))
print(a.reshape(9,1))

a=np.arange(1,7)
print(a.shape)
print(a.reshape(2,3))
print(a.reshape(3,2))

# Newaxis
a=np.arange(1,7)
print(a[np.newaxis,:])
print(a[:,np.newaxis])

#  Concatenation
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])

c=np.concatenate((a,b),axis=0)
print(c)
print(np.vstack((a,b))) # Stacks arrays vertically (row-wise)

c=np.concatenate((a,b),axis=1)
print(c)
print(np.hstack((a,b))) # Stacks arrays horizontally (column-wise)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6]])
c=np.concatenate((a,b),axis=0)
print(c)
c=np.concatenate((a,b.T),axis=1) # Transpose of b
print(c)


# Stacking
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.vstack((a,b)))
print(np.hstack((a,b)))


# Slicing
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[0:2,1:3])

a=np.array([10,21,32,43,54,65,76,87,98])
even=np.argwhere(a%2==0).flatten()
print(a[even])

# Copying
b=a.copy()
print(b)

# Iterating
for row in a:
    print(row)

for cell in a.flat:
    print(cell)

# Splitting
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.hsplit(a,3))
print(np.vsplit(a,3))

# Sorting
a=np.array([[9,8,7],[6,5,4],[3,2,1]])
print(np.sort(a,axis=0))
print(np.sort(a,axis=1))

# Masking
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a>5)
print(a[a>5])

# Broadcasting
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([1,2,3])
print(a+b)

# Vectorization
def f(x):
    return 1/(1+np.exp(-x))

a=np.array([1,2,3])
print(f(a))

# Data Science
# axis 0 row-wise, axis 1 column-wise
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.mean())
print(a.mean(axis=0))
print(a.mean(axis=1))

print(a.var())
print(a.var(axis=0))
print(a.var(axis=1))

print(a.std())
print(a.std(axis=0))
print(a.std(axis=1))

print(a.min())
print(a.min(axis=0))
print(a.min(axis=1))

print(a.max())
print(a.max(axis=0))
print(a.max(axis=1))

print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

# equal array
a=np.array([1,2,3])
b=np.array([1,2,3])
print(np.array_equal(a,b))
print(np.all(a==b))

