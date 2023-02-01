import csv
from pathlib import Path

def overhead_max_percentage():
    '''
    setup csv reading functions to calculate percentage of highest overhead cost
    by sorting each category name and add each amount to list
    no required parameters
    '''
    
    fp = Path.cwd()/ r"C:\Users\amias\IGP programming\csv_files\Overheads.csv"
    # setup csv reading functions skipping the first row
    with open('overheads.csv', 'r') as file:
        reader = csv.reader(file) 
        next(reader)

        # Lists to store expenses by category
        category = [['Depreciation Expense', 0.0],
                    ['Human Resource Expense', 0.0],
                    ['Interest Expense', 0.0],
                    ['Maintenance Expense', 0.0],
                    ['Marketing Expense', 0.0],
                    ['Overflow Expense - Retail', 0.0],
                    ['Overflow Expense - Warehouse', 0.0],
                    ['Penalty Expense', 0.0],
                    ['Rental Expense', 0.0],
                    ['Salary Expense', 0.0],
                    ['Shipping Expense', 0.0],
                    ['Total Expenses', 0.0]]    
        # sets category as row 1 and amount as row 3
        for row in reader:
            category_name = row[1]
            amount = float(row[3]) 
            # calculates total amount for all expenses
            category[11][1] += amount  
            # sorts each expense category by name
            if category_name == 'Depreciation Expense':
                category[0][1] += amount

            elif category_name == 'Human Resource Expense':
                category[1][1] += amount

            elif category_name == 'Interest Expense':
                category[2][1] += amount

            elif category_name == 'Maintenance Expense':
                category[3][1] += amount

            elif category_name == 'Marketing Expense':
                category[4][1] += amount

            elif category_name == 'Overflow Expense - Retail':
                category[5][1] += amount

            elif category_name == 'Overflow Expense - Warehouse':
                category[6][1] += amount         

            elif category_name == 'Penalty Expense':
                category[7][1] += amount  

            elif category_name == 'Rental Expense':
                category[8][1] += amount        

            elif category_name == 'Salary Expense':
                category[9][1] += amount

            elif category_name == 'shipping Expense':
                category[10][1] += amount 
    # initialize highest overhead and category
    highest_overhead = 0
    highest_overhead_category = ""
    # uses a for loop to calculate the highest overhead
    # makes a for loop for all categories excluding total expense 
    for idx in category[:len(category)-1]:
        if idx[1] > highest_overhead:
            highest_overhead = idx[1]
            highest_overhead_category = idx[0]
    # calculates the percentage of the highest overhead
    highest_overhead_percentage = highest_overhead / category[11][1] * 100

    return highest_overhead_percentage, highest_overhead_category
