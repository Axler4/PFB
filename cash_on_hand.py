import csv
from pathlib import Path
def cash_surplus_deficit():
    '''
    calculates if there is a defecit between each day and determines now much defecit there is
    no required parameters
    '''
    # initialize the list to store the totals
    totals = []
    deficits = []

    
    fp = Path.cwd()/ r"C:\Users\amias\IGP programming\csv_files\Cash on Hand.csv"

    # specifies the file path to the csv file
    

    with open(fp, 'r') as file:
        reader = csv.reader(file)
        next(reader)        
        
        # keep track of the current day and its total
        current_day = ""
        current_total = 0

        for row in reader:
            # check if the day has changed
            if row[0] != current_day:
                # if so, append the current total to the list and reset the total
                totals.append(current_total)
                current_total = 0

            # update the current day and add the amount to the total
            current_day = row[0]
            current_total += float(row[3])

        # append the last total to the list
        totals.append(current_total)
    # creates a for loop starting with 1 and ending with 1 index before total 
    for i in range(1, len(totals)-1):
        # calculates the difference in 
        diff = totals[i] - totals[i+1]
        # append differences less than 0, converts difference to absolute number for each day
        if diff < 0:
            deficits.append((91-i, abs(diff)))

    return deficits