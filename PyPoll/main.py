#Import dependencies
import os
import csv

#Call file location and open file as csv. 
poll_csv = os.path.join('election_data.csv')

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Read csv file as a list to iterate thorugh each row.
    poll_data = list(csvreader)


#Declare initial variables.
total_votes = 0
max_votes = 0
candidate_names = []
results = {}

#Loop through each row and evaluate whether or not the candidate's name already exists in the dictionary.
for row in poll_data [1:]:
    total_votes += 1
    candidate = row[2]
    #If the candidate exists, add a vote to his/her dictionary key.
    if candidate in results:
        results[candidate] += 1
    else:
    #If the candidate does not exist already, create his/her dictionary key and add the name to the candidate_names list.
        results[candidate] = 1
        candidate_names.append(row[2])

#Print the number of total votes to terminal.
print("Total votes: " + str(total_votes))
#For each candidate's dictionary key, get the total number of votes and calculate % of election votes. Then, print to terminal.
for name in candidate_names:
    print(name + ":  " + str(round((results[name] / total_votes) * 100,3)) + "%  (" + str(results[name]) + ")")
    #Evaluate whether or not each candidate has the maximum votes. Print the final maximum value.
    if(results[name]) > max_votes:
        winner = name
        max_votes = results[name]
    
print("Winner: " + winner)

#Print results accordingly to 'election_results.txt' file.
txtfile = open('election_results.txt', 'w')

txtfile.write("Total votes: " + str(total_votes) + "\n")
for name in candidate_names:
    txtfile.write(name + ":  " + str(round((results[name] / total_votes) * 100,3)) + "%  (" + str(results[name]) + ")\n")
    if(results[name]) > max_votes:
        winner = name
        max_votes = results[name]
    
txtfile.write("Winner: " + winner)
txtfile.close()

        
