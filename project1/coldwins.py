import os
import json
import csv
import sys
from requests import get
import matplotlib.pyplot as plt
import pandas as pd
import datetime




def main(argv):
  
    # Open CSV input file in read mode
    # Open CSV output file in write mode, overwrite if already exists
    csv_raw_input = open(argv[1], newline='')
    csv_raw_output = open(argv[2], "w");


    # Create CSV objects with raw files
    csv_file_input = csv.reader(csv_raw_input)
    csv_file_output = csv.writer(csv_raw_output)

    headers = ["team", "AVG.TEMP", "AVG.HUM" ]
    teams = []
    


    for row in csv_file_input:

       if(teams.count(row[1]) < 1) 



    //csv_file_output.writerow()

    # Close files at end
    csv_raw_input.close() 
    csv_raw_output.close()  






    # Don't know why, but the for loop below
    # would not work as written unless I closed
    # the CSV file and reopened it...
    #
    #csv_raw = open("hours.csv", "r")
   #csv_file = csv.reader(csv_raw)

   # print("\nPrint individual cells of CSV object.")
    #for row in csv_file:


        #for i in range(0, len(row)):
        #    print(row[i])
            
   # print("Close CSV file.\n")
   # csv_raw.close()




if __name__ == "__main__":
    main(sys.argv)