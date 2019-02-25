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

    for lines in csv_reader:
        months.append(lines[0])
        profitloss.append(lines[1])
       # print(profitloss)


    total_months = len(months[1:])
    
    total_profitloss = sum(list(map(int,profitloss[1:])))

    int_profitloss = list(map(int,profitloss[1:]))

    # use a loop to go through the profitloss list and calculate the differences into a new list called changes
    for n in range(1,len(int_profitloss)):
        changes = (int_profitloss[n] - int_profitloss[n-1])
        change_list.append(changes)
    
    #print(change_list)
    #calculate the change average, below we sum up the change list, and divide by the length(elements) in the list, we then use the round function to keep 2 decimal places
    average_changes = round(((sum(change_list)) / (len(change_list))),2)

    print(f'Financial Analysis')
    print(f'------------------------------------------------------------------')
    print (f'Total Months: {total_months}')
    print (f'Total: ${total_profitloss}')

    #print(int_profitloss)
    print(f'Average Changes: ${average_changes}')

   # print(profitloss[1])

    #csv_header = next(csv_reader)
    #print (f'CSV Header: {csv_header}')






    
