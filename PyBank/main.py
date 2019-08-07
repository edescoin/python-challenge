
# Import os module
import os
# To read CVS file
import csv

#Vhecking current Dir
cwkdir = os.getcwd()
#Append file directory and make a complete file path
filepath = os.path.join( cwkdir,'Resources','budget_data.csv')

#Variables
mcount = 0; total = 0; PreValue = 0; Diff = 0; DiffMax = 0; DiffMin = 0

#open csv file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f'--'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - PreValue
         #Tracking the increasing
         if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
         #Tracking the decreasing
         if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

         PreValue = iAmount   
         # Get total for the months
         mcount = mcount + 1
         total += int(Amount) 

# print all my results
print(f'Total Months : {mcount}')
#The total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {total}')
# Greatest increase in profit
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
# Greatest increase in profit
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')