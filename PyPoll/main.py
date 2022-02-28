import csv
import os

#load the file from and to the directory 
File_load = os.path.join("C:/Users/2mini/OneDrive/Python_Challenge/PyPoll/election_data.csv")
file_output = os.path.join("C:/Users/2mini/OneDrive/Python_Challenge/PyPoll/election_analysis.txt")

#total vote
total_vote = 0

#candidates options and vote counters
candidate_list = [] #total list
candidate_votes = {} #dictionary: keys=name; value = number of votes

#create variable for winning candidates and the count tracker
winning_candidate = "" # this going to change according to winner and count vote
winning_count = 0

#read the file from CSV file 
with open (File_load) as election_data:
    reader = csv.DictReader(election_data)
    
    #loop into each row
    for row in reader:
        #to add to total vote count and record each candidate name per row
        total_vote = total_vote + 1
        candidate_name = row["Candidate"]
        
        #for the candidate that the name differnt to previous candidate name
        if candidate_name not in candidate_list:
            #add to list by using append
            candidate_list.append(candidate_name)
            #add the tracking on each candidate name based on total vote
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#print and write to text file
with open(file_output, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"---------------\n"
        f"Total Votes : {total_vote}\n"
        f"---------------\n"
    )
    print(election_results) 
    #convert to text file
    txt_file.write(election_results)
    # Determine the winner by looping through the counts
    for candidate in candidate_votes:
        #total vote count and its percentage
        votes = candidate_votes.get(candidate) #to round closest decimal
        vote_percentage = float(votes)/float(total_vote) *100
        
        #count winning vote count and its candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        #totak candidate votes and its percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        
        #convert to text file
        txt_file.write(voter_output)
        
    #print the winning candidate
    winning_candidate_summary = (
        f"-----------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------\n"
    )
    print(winning_candidate_summary)
    
    #convert to text file
    txt_file.write(winning_candidate_summary)
    
        
            
            
            
            
            
            
        
        
        
