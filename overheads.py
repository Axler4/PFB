import csv

def overhead_max_percentage():
    with open('overheads.csv', 'r') as file:
        reader = csv.reader(file) 
        next(reader) # skip the header row

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

        for row in reader:
            category_name = row[1]
            amount = float(row[3]) 

            category[11][1] += amount  

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

    highest_overhead = 0
    highest_overhead_category = ""
    for idx in category[:len(category)-1]:
        if idx[1] > highest_overhead:
            highest_overhead = idx[1]
            highest_overhead_category = idx[0]
    highest_overhead_percentage = highest_overhead / category[11][1] * 100

    return highest_overhead_percentage, highest_overhead_category
