def get_permutation(list):
    if len(list)==1:
        return [list]
    if len(list)==0:
        return []
    permutation=[]
    for item in range(len(list)):
        current=list[item]
        rem_list=list[:item]+list[item+1:]
        rem_perm=get_permutation(rem_list)
        #Generate Permutation by adding first element
        for p in rem_perm:
            permutation.append([current]+p)
    return permutation

data=[1,2,3]
for perm in get_permutation(data):
    print(perm)


