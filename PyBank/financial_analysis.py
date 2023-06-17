import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
    
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    sum = 0
    for row in csvreader:
        print(row)
        net_amount = sum + row[1]
    print(net_amount)
