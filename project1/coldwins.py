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

    last_row = []

    # Headers for output file
    headers = ["team", "AVG.TEMP", "AVG.HUM" ]


    # games_played structure {team: numGames}
    # temps structure {team: sumHomeTemps}
    games_played = {}
    temps = {}



    numRow = 0


    # dict.keys()
    # dict.values()
    # dict.items()
    
    # team = row[1]
    # temp = row[5]
    # windchill = row[6]
    # total = 1-267

    for row in csv_file_input:

        last_row = row

        if(numRow != 0):
            
            # If team already in list, add to their totals
            if(row[1] in games_played):

                # Increment games played
                games_played[row[1]] += 1

                # If windchill present, add to temps min of the two
                if(row[6] != ''):
                   temps[row[1]] += min(int(row[5]), int(row[6]))

                # If no windchill present, add home temp to total
                else:
                    temps[row[1]] += int(row[5])

            # If team does not appear in list, initialize totals
            else:
                games_played[row[1]] = 1
                temps[row[1]] = int(row[5])

            numRow += 1
        else:
            numRow += 1

    # Remove superbowl temp/humidity data
    if(last_row[6] != ''):
        temps[last_row[1]] -= min(int(last_row[5]), int(last_row[6]))
    else:
        temps[last_row[1]] -= int(last_row[5])

    # Calculate AVG.TEMP
    for team in temps:

        # Don't include superbowl data in temp/humidity calculation
        if(team == last_row[1]):
            temps[team] = round(temps[team] / (games_played[team] - 1), 2)
        else:
            temps[team] = round(temps[team] / games_played[team], 2)


    


    # READY TO OUTPUT
    # AVG.TEMP --> temps



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