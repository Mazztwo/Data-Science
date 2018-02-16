# Data Science Project 2
# Alessio Mazzone

import csv
import sys


def main(argv):

    # python3 compute_active.py graph.csv   px     results.csv
    #                 argv[0]    argv[1]  argv[2]    argv[3]
    #                            graph   probability

    # Open CSV input file in read mode
    # Open CSV output file in write mode, overwrite if already exists
    csv_raw_input = open(argv[1], newline='')
    csv_raw_output = open(argv[3], "w")


    # Create CSV objects with raw files
    csv_file_input = csv.reader(csv_raw_input)
    csv_file_output = csv.writer(csv_raw_output)



    # Close files at end
    csv_raw_input.close() 
    csv_raw_output.close() 


if __name__ == "__main__":
    main(sys.argv)