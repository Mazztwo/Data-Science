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

### Part 4/5/6/7 #######
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

print("Close CSV file.\n")
csv_blank.close()

print("Open CSV file.")
csv_raw = open("hours.csv", "r")

print("Creating CSV object with raw file.")
csv_file = csv.reader(csv_raw)

print("Print all rows of CSV object.")
for row in csv_file:
    print(row)

# Don't know why, but the for loop below
# would not work as written unless I closed
# the CSV file and reopened it...
csv_raw.close()
csv_raw = open("hours.csv", "r")
csv_file = csv.reader(csv_raw)
###############################

print("\nPrint individual cells of CSV object.")
for row in csv_file:

    #This also works
    #print(" ".join(row))

    print("rawr")
    for i in range(0, len(row)):
        print(row[i])
        
print("Close CSV file.\n")
csv_raw.close()



