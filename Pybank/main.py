#module for createing file paths across operating systems
import os
#module for reading csv files
import csv

#since file is in the same folder as our main.py, I only need to designate file name
csvpath = os.path.join('budget_data.csv')

#define variables we will be working  with
months = []
profitloss = []
change_list= []

#method for reading of csv file

with open(csvpath, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader,None)
    for lines in csv_reader:
        months.append(lines[0])
        profitloss.append(lines[1])
        #print(profitloss)
        #print(months)


    total_months = len(months)
    
    total_profitloss = sum(list(map(int,profitloss)))
    int_profitloss = list(map(int,profitloss))
    # use a loop to go through the profitloss list and calculate the differences into a new list called changes
    for n in range(1,len(int_profitloss)):
        changes = (int_profitloss[n] - int_profitloss[n-1])
        change_list.append(changes)
    
    #print(change_list)
    #calculate the change average, below we sum up the change list, and divide by the length(elements) in the list, we then use the round function to keep 2 decimal places
    average_changes = round(((sum(change_list)) / (len(change_list))),2)
    max_change = max(change_list)
    min_change = min(change_list)
    minivalue = change_list.index(min_change)
    maxivalue = change_list.index(max_change)
    #Test out min and max values
    #print(minivalue)
    #print(maxivalue)
    #print(max_change)
    #print(min_change)
    minmonth = (months[minivalue + 1])
    maxmonth = (months[maxivalue + 1])

    print(f'Financial Analysis')
    print(f'------------------------------------------------------------------')
    print (f'Total Months: {total_months}')
    print (f'Total: ${total_profitloss}')

    #print(int_profitloss)
    print(f'Average Changes: ${average_changes}')
    print(f'Greatest Increase in Profits: {maxmonth} (${max_change})')
    print(f'Greatest Decrease in Profits: {minmonth} (${min_change})')









    
