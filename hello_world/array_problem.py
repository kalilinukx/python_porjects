# ls = [1, 43, 76, 23, 12, 32, 52, 68, 27, 87]
# y = []
# for item in ls:
#     if item == 68:
#         break
#     y.append(item)
# print(y)
import random_number
import numpy as np
import copy


ls = np.array([ 6, 0, 15, 17,  1, 12,  3,  8, 14, 18, 13, 11,  5,  2,  9,  7, 19,  4, 10, 16])
# [7, 0, 1, 3, 5, 8, 4, 9, 6, 2] perfect example of list
# [ 3 17 16 10 18 15 19  8  7  4  0  2  9  6  5 12 14 13 11  1] with 20 elements
# for i in range(10):
#     x = random.randint(1,100)
#     ls.append(x)

reversed_list = copy.deepcopy(ls)
# np.random.shuffle(ls)
print(ls)

print(ls[0:list(ls).index(max(ls))])

# print(np.partition(ls.flatten(), -2)[-2])


if list(ls).index(max(ls)) > list(ls).index(np.partition(ls.flatten(), -2)[-2]):
    print(ls[list(ls).index(np.partition(ls.flatten(), -2)[-2]):list(ls).index(max(ls))])
else:
    print(ls[::-1])
if list(ls).index(np.partition(ls.flatten(), -2)[-2]) > list(ls).index(np.partition(ls.flatten(), -3)[-3]):
    print(ls[list(ls).index(np.partition(ls.flatten(), -3)[-3]):list(ls).index(np.partition(ls.flatten(), -2)[-2])])
else:
    print("hey it wasn't quiet the required list")



