# import csv
# with open("data.csv","w+") as csvfiles:
#     writer = csv.writer(csvfiles)
#     writer.writerow(["Title","Description"])
#     writer.writerow(["Row 1","some desc"])
#     writer.writerow(["Title", "Description"])
#     writer.writerow(["Row 1", "some desc"])
#     writer.writerow(["Title", "Description"])
#     writer.writerow(["Row 1", "some desc"])
#     writer.writerow(["Title", "Description"])
#     writer.writerow(["Row 1", "some desc"])
import csv
with open("data.csv","w+") as csvfiles:
    writer = csv.writer(csvfiles)
    writer.writerow(["col 1","col 2"])
    writer.writerow(["data 1", "data 2"])

with open("data.csv", "w") as csvfiles:
    writer = csv.writer(csvfiles)
    writer.writerow(["col 1", "col 2"])
    writer.writerow(["data 1", "data 2"])

with open("data.csv","w") as csvfiles:
    writer = csv.writer(csvfiles)
    writer.writerow(["col 1","col 2"])
    writer.writerow(["data 1", "data 2"])