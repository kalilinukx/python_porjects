# an iterators is an objects that contains a countable number of values .
# list ,tuples ,dictionaries,and sets are all iterable objects have a iter()  method which is used to get an error
myster="banana"
myit=iter(myster)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#Looping through an iterator we can also usea for loop to iterate through an iterable object
mytuple=('apple','banana','cherry')
for x in mytuple:
    print(x)