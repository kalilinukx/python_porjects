import  csv

from path_lib import file

file=open("phonebook.csv","a")
name=input("name:")
number=int(input("number:"))
writer=csv.writer(file)
writer.writerow((name,number))
file.close()
