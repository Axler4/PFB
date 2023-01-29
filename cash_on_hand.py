from pathlib import Path
import matplotlib.pyplot as plt 
import csv

fp = Path.cwd()/"Cash_On_Hand.csv"

sums = {}

with open(fp) as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for column in reader:
        day, amount = column
        if day in sums:
            sums[day] += float(amount)
        else:
            sums[day] = float(amount)

# Print the sums for each day
for day, amount in sums.items():
    print(f'{day}: ${amount}')
