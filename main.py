import overheads as ohs
import cash_on_hand as coh
import profit_loss as pfl

ohs_percent, ohs_cat = ohs.overhead_max_percentage()
deft = coh.cash_surplus_deficit()
np = pfl.extract_profit_loss()

with open("summary_report.txt", "a") as file:
    file.write(f"[HIGHEST OVERHEADS] {ohs_cat.title()}: {ohs_percent:.2f}% \n")
    
    for i in range(len(deft)):
        file.write(f"[CASH DEFECIT] DAY: {deft[i][0]}, AMOUNT: USD{deft[i][1]:.2f}\n")
        
    for ix in range(len(np)):
        file.write(f"[PROFIT DEFECIT] DAY: {np[ix][0]}, AMOUNT: USD{abs(np[ix][1]):.2f}\n")
