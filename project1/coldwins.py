import os
import json
import csv
from requests import get
import matplotlib.pyplot as plt
import pandas as pd
import datetime



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


