def hasDuplicates(list):
  flag = 0
  for i in range (len(list)):
     for j in range (i + 1, len(list)):
         if (list[i] == list[j]):
             flag = 1
  if (flag == 1):
     return True
  else:
     return False



print(hasDuplicates([1.2,3.4,5.6,7.5,1.2]))