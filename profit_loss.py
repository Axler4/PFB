import csv

def extract_profit_loss(): 
    expenses = []
    revenue = []
    cost_of_goods = []
    net_profit = []
    profit_defecit = []
    days = range(90,0,-1)
    with open("Overheads.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        current_day = ""
        current_total = 0

        for row in reader:
            if row[0] != current_day: 
                current_day = row[0]
                expenses.append(current_total)
                current_total = 0
            current_total += float(row[3])

    with open("Profit & Loss.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)
        current_day = ""
        revenue_total = 0
        cogs_total = 0
        
        for row in reader:
            if row[0] != current_day:
                current_day = row[0]
                revenue.append(revenue_total)
                cost_of_goods.append(cogs_total)
                revenue_total = 0
                cogs_total = 0                    
            revenue_total += float(row[4])
            cogs_total += float(row[5])
                
    expenses.pop(0)
    revenue.pop(0)
    cost_of_goods.pop(0)

    for xp, rev, cog in zip(expenses, revenue, cost_of_goods):
        net_profit.append(rev-xp-cog)
        
    for ix in range(1,len(net_profit)):
        current_profit = net_profit[ix-1] - net_profit[ix]
        if current_profit<0:
            defecit_index = ix-1
            defecit_days = days[defecit_index]
            profit_defecit.append([defecit_days,current_profit])
            
    return profit_defecit

