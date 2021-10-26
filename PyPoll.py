# The data we will need to retireve 
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a save a file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#create a variable to define the accumulation of total votes
total_votes = 0
#declare a new list for the candidates
candidate_options = []
#declare the empty dictionary
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #read the header row
    headers = next(file_reader)

    # add the total vote count. STandard python format to increment by one is number = numer + 1 OR number +=1
    for row in file_reader:
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #add candidate name to the candidate list 
        if candidate_name not in candidate_options:
            #if not in the list, then add it to the list
            candidate_options.append(candidate_name)
            #AND begin tracking the candidates votes
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count. This needs to be out of the if statement and in the for loop to keep adding incrementally
        candidate_votes[candidate_name] += 1
    #print the candidate list of names 
    print(candidate_votes)
    #iterate through the candidate list by name
    for candidate_name in candidate_options:
        #retieve count votes for a candidate
        votes = candidate_votes[candidate_name]
        #calculate the vote percentage
        vote_percentage = float(votes)/float(total_votes)*100
        #print the result with a full sentence
        print(f"{candidate_name}: received {vote_percentage:,.2f}% of the vote")



