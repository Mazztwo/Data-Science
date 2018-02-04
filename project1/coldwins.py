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


    # games_played --> {team: numGames}
    # temps --> {team: sumHomeTemps}
    # humidity --> {team: sumHomeHumidity} 
    games_played = {}
    temps = {}
    humidity = {}
    per_wins = {}
    games_home = {}
    games_away = {}



    numRow = 0


    # dict.keys()
    # dict.values()
    # dict.items()
    
    # home team = row[1]
    # home score = row[2]
    # away team = row[3]
    # away score = row[4]
    # temp = row[5]
    # windchill = row[6]
    # humidity = row[7]
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

                # Increment humidity
                if( row[7] == '' ):
                    humidity[row[1]] += 0
                elif( len(row[7])  == 2 ):
                    humidity[row[1]] += int(row[7][0])
                else:
                    humidity[row[1]] += int(row[7][0:2])

                # Percent wins
                 

            # If team does not appear in list, initialize totals
            else:
                games_played[row[1]] = 1
                temps[row[1]] = int(row[5])

                # Humidity length can be:
                # 0 --> 0% humidity --> ''
                # 2 --> x% humidity --> x%
                # 3 --> xx% humidity --> xx%
                if( row[7] == '' ):
                    humidity[row[1]] = 0
                elif( len(row[7])  == 2 ):
                    humidity[row[1]] = int(row[7][0])
                else:
                    humidity[row[1]] = int(row[7][0:2])

            # Percent wins
            # If home wins
            if(row[2] > row[4]):
                if(row[1] in per_wins):
                    per_wins[row[1]] += 1
                else:
                    per_wins[row[1]] = 1
                    
                if(row[3] not in per_wins):
                    per_wins[row[3]] = 0

            # If away wins
            else:
                if(row[3] in per_wins):
                    per_wins[row[3]] += 1
                else:
                    per_wins[row[3]] = 1
                    
                if(row[1] not in per_wins):
                    per_wins[row[1]] = 0
                           
               
            # Total games home and away
            if(row[1] in games_home):
                games_home[row[1]] += 1
            else:
                games_home[row[1]] = 1   

            if(row[3] in games_away):
                games_away[row[3]] += 1
            else:
                games_away[row[3]] = 1
           

            numRow += 1
        else:
            numRow += 1

    # Remove superbowl temp/humidity data
    if(last_row[6] != ''):
        temps[last_row[1]] -= min(int(last_row[5]), int(last_row[6]))
    else:
        temps[last_row[1]] -= int(last_row[5])

    if(last_row[7] != ''):
        if( len(last_row[7])  == 2 ):
            humidity[last_row[1]] -= int(last_row[7][0])
        else:
            humidity[last_row[1]] -= int(last_row[7][0:2])

    # Calculate AVG.TEMP
    for team in temps:

        # Don't include superbowl data in temp/humidity calculation
        if(team == last_row[1]):
            temps[team] = round(temps[team] / (games_played[team] - 1), 2)
        else:
            temps[team] = round(temps[team] / games_played[team], 2)

    # Calculate AVG.HUM
    for team in humidity:

        # Don't include superbowl data in temp/humidity calculation
        if(team == last_row[1]):
            humidity[team] = round(humidity[team] / (games_played[team] - 1), 2)
        else:
            humidity[team] = round(humidity[team] / games_played[team], 2)

    # Calculate PER.WINS
    for team in per_wins:
        per_wins[team] = round( (per_wins[team] / (games_home[team] + games_away[team]))*100 , 2)

    # READY TO OUTPUT
    # AVG.TEMP --> temps
    # AVG.HUM --> humidity
    # PER.WINS --> per_wins
    

    print(per_wins)


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