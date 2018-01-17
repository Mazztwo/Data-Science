# Alessio Mazzone
# CS 1656 - Data Science
# Recitation 1: Python Tutorial

import os
import json
import csv
from requests import get


### Part 1 #######


##################

### Part 2 #######


##################

### Part 3 #######


##################

### Part 4 - Convert to CSV #######
print("Opening JSON file and load data.")
json_file = open("hours.json", 'r')
json_data = json.load(json_file) # or json.load(open("file.json", 'r'))

print("Close JSON file.")
json_file.close()

print("Creating blank CSV file.")
csv_blank = open("hours.csv", "w+")

print("Converting JSON to CSV.")
csv_writer = csv.writer(csv_blank)

# Write the header row
csv_writer.writerow(json_data[0].keys())

# For every line in the JSON data, write 
# the value of that line to the CSV file.
for line in json_data: 
    csv_writer.writerow(line.values())

print("Close CSV file.")
csv_blank.close()

##################

### Part 5 #######


##################

### Part 6 #######


##################

### Part 7 #######


##################


