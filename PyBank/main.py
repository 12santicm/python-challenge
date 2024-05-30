import csv
import os

# Variables
total_months = 0
net_total = 0
previous_profit_loss = None
monthly_changes = []
greatest_increase = ('', 0)
greatest_decrease = ('', 0)


budget_data_csv = os.path.join('Resources1', 'budget_data.csv')  

# Open and read the CSV file
with open(budget_data_csv) as file:
    reader = csv.reader(file)
    header = next(reader) 

    for row in reader:
        date = row[0]
        profit_loss = int(row[1])

        # Increment the total number of months
        total_months += 1

        # Add to the net total amount of "Profit/Losses"
        net_total += profit_loss

        # Calculate the monthly change
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            monthly_changes.append(change)

            # Check for greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase = (date, change)

            # Check for greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease = (date, change)

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average of the changes in "Profit/Losses"
if len(monthly_changes) > 0:
    average_change = sum(monthly_changes) / len(monthly_changes)
else:
    average_change = 0

# Prepare the results
results = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
)

# Print the results to the terminal
print(results)


# Export the results to a text file
with open('financial_analysis.txt', 'w') as file:
    file.write(results)
