
#Module for reading csv files
import csv
#Module that allows us to create file paths
import os

csvpath = os.path.join("election_data.csv")

#Define Variables for lists that we will be working with
voters =[]
candidates = []

#Reading election data

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    next(csvreader,None)
    for lines in csvreader:
        voters.append(lines[0])
        candidates.append(lines[2])
    #print(voters)
    #print(candidates)
#Determine the number of voters by taking a count(using lens function) of voters list, which is made up of the voter IDs 
total_votes = len(voters)
#print total_votes to test answer
unique_candidates = list(set(candidates))
#print(unique_candidates)# to verify list

#define counters from above we know there are 4 individual candidates, so we need 4 counters
counter_0 = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0

for x in candidates:
        if x == unique_candidates[0]:
            counter_0 = counter_0 + 1
        elif x == unique_candidates[1]:
            counter_1 = counter_1 + 1
        elif x == unique_candidates[2]:
            counter_2 = counter_2 + 1
        else:
            counter_3 = counter_3 + 1
    
#print(counter_0)
# calculate percentage of votes
percentage_0 = counter_0 / total_votes
#print(counter_1)
percentage_1 = counter_1 / total_votes
#print(counter_2)
percentage_2 = counter_2/ total_votes
#print(counter_3)
percentage_3 = counter_3/ total_votes
candidate_votes = [counter_0, counter_1, counter_2, counter_3]
sorted_votes = sorted(candidate_votes, reverse=True)
percent_votes = ["{:.2%}".format(percentage_0), "{:.2%}".format(percentage_1), "{:.2%}".format(percentage_2), "{:.2%}".format(percentage_3)]
#print(percentage_0)
#print(percentage_1)
#print(percentage_2)
#print(percentage_3)
#print(percent_votes)
#Print out of our Election Results
print("Election Results")
print("------------------------------------------------------------")
print(f'Total Votes: {total_votes}')
print(f'------------------------------------------------------------')
print(f'{unique_candidates[0]}: {percent_votes[0]} ({counter_0})')
print(f'{unique_candidates[1]}: {percent_votes[1]} ({counter_1})')
print(f'{unique_candidates[2]}: {percent_votes[2]} ({counter_2})')
print(f'{unique_candidates[3]}: {percent_votes[3]} ({counter_3})')
print(f'------------------------------------------------------------')
print(f'Khan is the winner!')

outpath = os.path.join("pypolltest.txt")

with open(outpath,'w',newline='') as textfile:
    csv_writer = csv.writer(textfile, delimiter=',')

    csv_writer.writerow([f'Election Results'])
    csv_writer.writerow([f'------------------------------------------------------------------'])
    csv_writer.writerow([f'Total Votes: {total_votes}'])
    csv_writer.writerow([f'------------------------------------------------------------------'])
