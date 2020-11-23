import random_number
import numpy as np
import copy


ls = np.array([4, 8, 3,14,15, 0, 6, 1, 2, 7,16,21, 9, 5,10,13,11,12,22,20,17,19,18])
# [7 0 1 3 5 8 4 9 6 2] perfect example of list
# [ 3 17 16 10 18 15 19  8  7  4  0  2  9  6  5 12 14 13 11  1] with 20 elements
# for i in range(10):
#     x = random.randint(1,100)
#     ls.append(x)

reversed_list = copy.deepcopy(ls)
np.random.shuffle(ls)
print(ls)

print(ls[0:list(ls).index(max(ls))])

# print(np.partition(ls.flatten(), -2)[-2])
# new = ls[0:list(ls).index(np.partition(ls.flatten(), -3)[-3])]

#
if list(ls).index(max(ls)) > list(ls).index(np.partition(ls.flatten(), -2)[-2]):
    print(ls[list(ls).index(np.partition(ls.flatten(), -2)[-2]):list(ls).index(max(ls))])
else:
    arr = ls[list(ls).index(np.partition(ls.flatten(), -2)[-2]):]
    new_arr = copy.deepcopy(ls[0:list(ls).index(max(ls))])
    final_arr = np.hstack((arr, new_arr))
    print(final_arr)
if list(ls).index(np.partition(ls.flatten(), -2)[-2]) > list(ls).index(np.partition(ls.flatten(), -3)[-3]):
    print(ls[list(ls).index(np.partition(ls.flatten(), -3)[-3]):list(ls).index(np.partition(ls.flatten(), -2)[-2])])
else:
    x = ls[list(ls).index(np.partition(ls.flatten(), -3)[-3]):]

    new = copy.deepcopy(ls[0:list(ls).index(np.partition(ls.flatten(), -2)[-2])])
    z = np.hstack((x, new))
    print(z)
