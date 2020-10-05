# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes=0

# Candidate options and candidate votes
candidate_options=[]
candidate_votes={}

#Winnind Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    hearders=next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes+= 1

        # Print the candidate name from each row.
        candidate_name=row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            #Add candidate the candidate name to the condidate list
            candidate_options.append(candidate_name)
            #begin tracking that candidates votes
            candidate_votes [candidate_name]= 0
        # add new line of votes to teh candidates count
        candidate_votes[candidate_name] += 1
            
print(candidate_votes)

for candidate_name in candidate_votes:
    votes=candidate_votes[candidate_name]
    vote_percentage= float (votes)/float (total_votes)*100
  # print (f"{candidate_name}: recieved {vote_percentage} % of the votes")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name




#  To do: print out the winning candidate, vote count and percentage to
#   terminal

#print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#print (winning_candidate ,"has won the election by recieving", winning_percentage ," % of", winning_count, "votes") 
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)





