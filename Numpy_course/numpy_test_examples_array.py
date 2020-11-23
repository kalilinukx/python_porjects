import numpy as np
import random as rd
x = np.array([12,34,6])
print(x)

Z = np.arange(9)
print(Z)
np.arange(9).reshape(9,1)
np.random.randint(0,9,(3,3)).reshape(3,3)
np.linspace(1,2,5)
import numpy as np
Z=np.mgrid[0:3,0:3]
print(Z)