#Import dependencies
import os
import csv

#Call file location and open file as csv. 
bank_csv = os.path.join('budget_data.csv')

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Read csv file as a list to iterate thorugh each row.
    bank_data = list(csvreader)
    
#Declare initial variables.
var_list = []
months_list = []
total = []
opening_value = int(bank_data[1][1])

#Loop through each row and get all month names, variations and total profit/loss for each month. Restart the opening value each time.
for row in bank_data[1:]:
    months_list.append(row[0])
    variation = int(row[1]) - opening_value
    total.append(int(row[1]))
    var_list.append(variation)
    opening_value = int(row[1])
    
#Print results to read in terminal.
print("Total months analyzed: " + str(len(months_list)))
print("Total Profits/Losses " + str(sum(total)))
print("Average variation: " + str(round(sum(var_list) / len(var_list),2))) 
print("Maximum variation: " + months_list[var_list.index(max(var_list))] + "    (" + str(max(var_list)) + ")")
print("Minimum variation: " + months_list[var_list.index(min(var_list))] + "    (" + str(min(var_list)) + ")")

#Print results in 'bank_results.txt' new file.
txtfile = open('bank_results.txt', 'w')

txtfile.write("Total months analyzed: " + str(len(months_list)) + "\n")
txtfile.write("Total Profits/Losses " + str(sum(total)) + "\n")
txtfile.write("Average variation: " + str(round(sum(var_list) / len(var_list),2)) + "\n") 
txtfile.write("Maximum variation: " + months_list[var_list.index(max(var_list))] + "    (" + str(max(var_list)) + ")\n")
txtfile.write("Minimum variation: " + months_list[var_list.index(min(var_list))] + "    (" + str(min(var_list)) + ")")

txtfile.close()