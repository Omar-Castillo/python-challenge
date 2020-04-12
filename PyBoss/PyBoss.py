#we need to import module for reading csv files and datetime
import csv
import os
from datetime import datetime
#we need to create a path for our csv file
csv_file = "employee_data.csv"
file_output = "pyboss_final.csv"

#create empty lists for new column names
employee_id= []
first_name = []
last_name = []
dob = []
ssn = []
state = []
name = []

#create a list for state abbrev.
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#improved reading using CSV module

with open(csv_file) as csvfile:

    #CSV reader specifies delimter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #we read the header row first
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    #read each row of data after the header, we append the data into blank lists
    for row in csvreader:
        #you can append the data directly for these columns
        employee_id.append(row[0])

        #append DOB into new list, then work on formating string into date
        date_info = datetime.strptime(row[2], '%Y-%m-%d')
        formatted_date = date_info.strftime('%m/%d/%Y')
        dob.append(formatted_date)
        
        #format the SSN number to hide the first five numbers
        ssn_number = row[3]
        ssn_secure = '***-**-' + ssn_number[-4:]
        ssn.append(ssn_secure)

        #now we need abbrev state names
        state_short = us_state_abbrev[row[4]]
        state.append(state_short)
        
        #create a list of name column split by space, append 
        full_name = row[1].split(" ")
        first_name.append(full_name[0])
        last_name.append(full_name[1])


    #test
    # print(employee_id)
    # print(first_name)
    # print(dob)
    # print(ssn)
    # print(state)
    
    #zip lists together 
    cleaned_csv = zip(employee_id,first_name,last_name,dob,ssn,state)

    #write all of the election data to csv
    with open(file_output, "w", newline='') as final_file:
        writer = csv.writer(final_file)

        #write the header row
        writer.writerow(["Emp ID","First Name","Last Name", "DOB", "SSN", "State"])

        #write in zipped rows
        writer.writerows(cleaned_csv)
