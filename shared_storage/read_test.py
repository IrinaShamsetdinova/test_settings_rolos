import csv
with open("/home/coder/project/.rolos_storages/shared/450a010a0e3242b996dee9358da88399.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print (row)