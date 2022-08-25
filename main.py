# save a CSV file
# library csv files
import csv
# library for create numbers random
import random

csvFile = open('test.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('SR', 'ID', 'Price'))
    # for to write in csv file numbers random
    for i in range(10):
        writer.writerow((i+1, random.randint(1, 100),
                         random.randint(100, 1000)))
finally:
    csvFile.close()






