import csv
import os

# Initialize variables
total_votes = 0
candidate_votes = {}

# Construct the file path
election_data_csv = os.path.join('Resources2', 'election_data.csv')

# Open and read the CSV file
with open(election_data_csv, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    for row in reader:
        total_votes += 1
        candidate = row[2]
        
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the results
results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

# Find the winner
winner = None
winner_votes = 0

for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    results += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

results += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print the results to the terminal
print(results)

# Export the results to a text file
output_file = os.path.join('Resources2', 'election_results.txt')
with open(output_file, 'w') as file:
    file.write(results)
