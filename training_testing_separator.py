import csv

# read csv

data_file = csv.reader(open('./data.csv'), delimiter=',')

trainX = []
trainY = []
testX = []
testY = []

# separate file

fg = 0

for row in data_file:
    if fg == 0:
        trainX.append(row[1:3])
        trainY.append(row[0])
    else:
        testX.append(row[1:3])
        testY.append(row[0])
    fg = 1 - fg

with open('./trainX.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in trainX:
        writer.writerow(line)

with open('./trainY.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in trainY:
        writer.writerow([line])

with open('./testX.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in testX:
        writer.writerow(line)

with open('./testY.csv', "w") as csv_file:
    writer = csv.writer(csv_file)
    for line in testY:
        writer.writerow([line])
