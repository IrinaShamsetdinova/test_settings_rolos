import csv
with open("/home/coder/project/poker_hand_train_true.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print (row)