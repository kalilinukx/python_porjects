def getAverage():
    l1 = [1, 4, 9, 10, 23]
    avg = sum(l1) / len(l1)
    return avg


avg = getAverage()
print(avg)

# remove items from list
def removeList():
  l1 = [1, 4, 9, 10, 23]
  l2 = [4, 9]
  # del l1[4,9]
  l1 = [ele for ele in l1 if ele not in l2]
  ## Write your code here
  return l1

def removeList():
  l1 = [1, 4, 9, 10, 23]
  l2 = [4, 9]
  # del l1[4,9]
  l1 = [ele for ele in l1 if ele not in l2]
  ## Write your code here
  return l1


# In python, here’s how to create a list with the squared numbers of another list.
print([x*x for x in range(4)])

# this is going to create a square

def getSquare():
  ## Write your code here
  l1 = [x*x for x in range(1,11)] ## Create your list here
  return l1