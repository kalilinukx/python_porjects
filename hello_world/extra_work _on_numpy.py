import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [6, 7, 12, 11, 43, 22, 3]])
print(a)
c = np.ones([5, 5], dtype='int')
z = np.zeros([3, 3], dtype="int")
print(c)
z[1, 1] = 9
print(z)
c[1:4, 1:4] = z
print(c)
