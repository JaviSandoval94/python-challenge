# Introduction
Python scripting can come handy in real world situations when data volume and complexity requires more than manual calculations and even basic analysis on spreadsheets such as Excel. This is a practice project divided into two challenges, related directly to real world applications:

## PyBank
The Python script analyzes the data records to calculate each of the following:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The average of the changes in "Profit/Losses" over the entire period
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in losses (date and amount) over the entire period

## PyPoll
This challenge analyzes the election results of a fictional rural town hall. The expected results are the following
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.

Each challenge is saved into an individual folder within the repository. Each folder contains a `main.py` file containing the analysis script and the results of both challenges are exported to a `.txt` file as a summary.

# Data set
This is a practice exercise done using the `election_data.csv` (`Voter ID`, `Country` and `Candidate`) and `budget_data.csv` (consisting of the following fields: `Date`, `Profit/Losses`) files as provided by the Tecnológico de Monterrey Data Analytics Bootcamp in the February - August 2020 term. Both files can be found in the corresponding folders within this repository.

# Code description
Run the `main.py` files contained in the folders of each challenge, make sure to have all the files available within the folder. The script will print the results on screen and export the results in the corresponding `.txt` files.

The results obtained were the following:
PyBank:
````
Total months analyzed: 86
Total Profits/Losses 38382578
Average variation: -2288.2
Maximum variation: Feb-2012    (1926159)
Minimum variation: Sep-2013    (-2196167)
````

PyPoll:
````
Total votes: 3521001
Khan:  63.0%  (2218231)
Correy:  20.0%  (704200)
Li:  14.0%  (492940)
O'Tooley:  3.0%  (105630)
Winner: Khan
````

# Conclusions
This project gives a good insight of the real world applications of Python. It is also a great motivation, since you don't have to be a super experienced programmer to start implementing problem solutions in everyday situations!
