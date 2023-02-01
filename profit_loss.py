import csv
from pathlib import Path

def extract_profit_loss(): 
    '''
    takes the revenue for each day and subtracts the cost of goods sold and expenses from it.
    Final profit is then compared with the following dya to see if there is a defecit in profit and if there is by how much
    no required parameters
    '''
    # creates empty list for each category
    expenses = []
    revenue = []
    cost_of_goods = []
    net_profit = []
    profit_defecit = []
    # creates range starting from day 90 to 1 with -1 step
    days = range(90,0,-1)
    
    
    fp = Path.cwd()/ r"C:\Users\amias\IGP programming\csv_files\Profit & Loss.csv"
    # setup csv reading function
    with open(fp, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        # initialises curent day and total
        current_day = ""
        current_total = 0

        for row in reader:
            # check if the day has changed
            if row[0] != current_day: 
                current_day = row[0]
                # append current total to expenses
                expenses.append(current_total)
                current_total = 0
            current_total += float(row[3])
    # setup csv reading function 
    fp = Path.cwd()/ r"C:\Users\amias\IGP programming\csv_files\Profit & Loss.csv"
    with open(fp, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        # initialise values 
        current_day = ""
        revenue_total = 0
        cogs_total = 0
        
        for row in reader:
            #checks if the day has changed
            if row[0] != current_day:
                current_day = row[0]
                # apend revenue to total revenue and cost of goods 
                revenue.append(revenue_total)
                cost_of_goods.append(cogs_total)
                # resets total values
                revenue_total = 0
                cogs_total = 0                    
            revenue_total += float(row[4])
            cogs_total += float(row[5])
    # removes the first 0 for the 3 items           
    expenses.pop(0)
    revenue.pop(0)
    cost_of_goods.pop(0)
    # zips expenses, cost of goods sold and revenue together
    for xp, rev, cog in zip(expenses, revenue, cost_of_goods):
        # append profit to net profit
        net_profit.append(rev-xp-cog)
    # creats a for loop to calculate the profit defecit for each day
    for ix in range(1,len(net_profit)):
        current_profit = net_profit[ix-1] - net_profit[ix]
        if current_profit<0:
            defecit_index = ix-1
            # find the days that have defecit
            defecit_days = days[defecit_index]
            # append profit defecit with defecit days and current profit
            profit_defecit.append([defecit_days,current_profit])
            
    return profit_defecit

