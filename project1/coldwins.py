import csv
import sys






def main(argv):
  
    # Open CSV input file in read mode
    # Open CSV output file in write mode, overwrite if already exists
    csv_raw_input = open(argv[1], newline='')
    csv_raw_output = open(argv[2], "w")

    # Create CSV objects with raw files
    csv_file_input = csv.reader(csv_raw_input)
    #csv_file_output = csv.writer(csv_raw_output)

    #headers = ["team", "AVG.TEMP", "AVG.HUM" ]
    teams = {}
    numRow = 0


    # dict.keys()
    # dict.values()
    # dict.items()
    
    # team = row[1]
    # temp = row[5]
    # windchill = row[6]

    for row in csv_file_input:

        if(numRow != 0):

            if(row[1] in teams):
                teams[row[1]] += 1
            else:
                teams[row[1]] = 1

            numRow += 1
        else:
            numRow += 1

    # Check superbowl, last game, and remove data from those
    #   

    print(teams.items())
    print("NUM ROWS: %d" % (numRow))



    #csv_file_output.writerow()

    # Close files at end
    csv_raw_input.close() 
    csv_raw_output.close()  











if __name__ == "__main__":
    main(sys.argv)











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