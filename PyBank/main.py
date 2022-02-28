import os
import csv

#load the file from resources to the directory
file_load = os.path.join ("C:/Users/2mini/OneDrive/Python_Challenge/PyBank/budget_data.csv")
file_output = os.path.join("C:/Users/2mini/OneDrive/Python_Challenge/PyBank/budget_analysis.txt")

#label the variables
greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999]   
month_of_change = []
profit_loss_change = []
prev_profit_loss = 0
total_month = 0
total_profit_loss = 0

#read the file from budget analysis
with open (file_load, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        
        #track the totals
        total_month = total_month + 1
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
        current_value = int(row["Profit/Losses"])
        
        #track the revenue change
        revenue_change = int(current_value - prev_profit_loss)
        
        profit_loss_change.append(revenue_change)
        month_of_change = month_of_change + [row["Date"]]
        prev_profit_loss = int(row["Profit/Losses"])
        #profit_loss_change = profit_loss_change + [revenue_change]
        
        total_profit_loss=total_profit_loss + revenue_change
        #calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change
            
        #calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change
            
#calculate average revenue change
revenue_ave = sum(profit_loss_change) /len(month_of_change)
        
#Output summary
output = (
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {total_month}\n"
    f"Total: $ {total_profit_loss}\n"
    f"Average Change: $ {revenue_ave:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
        
#print the result
#print(output)

#export to text file
print(output)
with open(file_output, "w") as txt_file:
   txt_file.write(output)  

   file_output