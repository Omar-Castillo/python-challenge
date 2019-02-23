#module for createing file paths across operating systems
import os
#module for reading csv files
import csv

csvpath = os.path.join('budget_data.csv')

months = []
profitloss = []

#method for reading of csv file

with open(csvpath, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for lines in csv_reader:
        months.append(lines[0])
        profitloss.append(lines[1])

    
    total_months = len(months)
    total_profitloss = sum(int(profitloss))
    print (total_months)
    print (total_profitloss)


    
    #csv_header = next(csv_reader)
    #print (f'CSV Header: {csv_header}')






    
