# 8nmyca9rja9ohm40s711dg2qd
ran = ['sum', 'range','array','tuple']
import builtins
for i in ran:
    if i not in dir(builtins):
        print(i)