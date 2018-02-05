import csv
import sys



def addDecimals(num):

    if( len(str(num).rsplit('.')[-1]) == 2 ):
        return num
    elif( len(str(num).rsplit('.')[-1]) == 1 ):
        num = str(num) + "0"
        return str(num)
    elif( len(str(num).rsplit('.')[-1]) == 0 ):
        num = str(num) + ".00"
        return str(num)
    else:
        pass



def main(argv):
  
    # Open CSV input file in read mode
    # Open CSV output file in write mode, overwrite if already exists
    csv_raw_input = open(argv[1], newline='')
    csv_raw_output = open(argv[2], "w")

    # Create CSV objects with raw files
    csv_file_input = csv.reader(csv_raw_input)
    csv_file_output = csv.writer(csv_raw_output)

    last_row = []

    # Headers for output file
    output_headers = ["team_name", "AVG.TEMP", "AVG.HUM", "PER.WINS", "PER.WINS.HOME", "PER.WINS.AWAY", "PER.WINS.TEMP.LESS", "PER.WINS.TEMP.MORE", "PER.WINS.HUM.LESS", "PER.WINS.HUM.MORE"]

    games_played = {}
    temps = {}
    humidity = {}
    per_wins = {}
    games_home = {}
    games_away = {}
    per_wins_home = {}
    per_wins_away = {}
    per_wins_temp_less = {}
    per_wins_temp_more = {}
    per_wins_hum_less = {}
    per_wins_hum_more = {}

    numRow = 0

    # dict.keys()
    # dict.values()
    # dict.items()


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
            if(int(row[2]) > int(row[4])):
                if(row[1] in per_wins):
                    per_wins[row[1]] += 1
                else:
                    per_wins[row[1]] = 1          
                if(row[3] not in per_wins):
                    per_wins[row[3]] = 0
                if(row[1] in per_wins_home):
                    per_wins_home[row[1]] += 1
                else:
                    per_wins_home[row[1]] = 1
            # If away wins
            else:
                if(row[3] in per_wins):
                    per_wins[row[3]] += 1
                else:
                    per_wins[row[3]] = 1  
                if(row[1] not in per_wins):
                    per_wins[row[1]] = 0
                if(row[3] in per_wins_away):
                    per_wins_away[row[3]] += 1
                else:
                    per_wins_away[row[3]] = 1
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
    # Calculate PER.WINS.HOME
    for team in per_wins_home:
        per_wins_home[team] = round((per_wins_home[team] / games_home[team])*100,2)
    # Calculate PER.WINS.HOME
    for team in per_wins_away:
        per_wins_away[team] = round((per_wins_away[team] / games_away[team])*100,2)    
    # Reset Iterator
    csv_raw_input.close() 
    csv_raw_input = open(argv[1], newline='')
    csv_file_input = csv.reader(csv_raw_input)
    numRow = 0
    # Calculate PER.WINS.TEMP.LESS    
    for row in csv_file_input:
        if(numRow != 0):
            if(int(row[2]) > int(row[4])):
                if(row[6] != ''):
                    curr_temp = min(int(row[5]),int(row[6]))
                else:
                    curr_temp = int(row[5])
                if(temps[row[1]] > curr_temp):
                    if(row[1] in per_wins_temp_less):
                        per_wins_temp_less[row[1]] += 1
                    else:
                        per_wins_temp_less[row[1]] = 1
                else:
                    if(row[1] in per_wins_temp_more):
                        per_wins_temp_more[row[1]] += 1
                    else:
                        per_wins_temp_more[row[1]] = 1 
                if( row[7] == '' ):
                    curr_humidity = 0
                elif( len(row[7])  == 2 ):
                    curr_humidity= int(row[7][0])
                else:
                    curr_humidity= int(row[7][0:2])        
                if(humidity[row[1]] > curr_humidity):
                    if(row[1] in per_wins_hum_less):
                        per_wins_hum_less[row[1]] += 1
                    else:
                        per_wins_hum_less[row[1]] = 1
                else:
                    if(row[1] in per_wins_hum_more):
                        per_wins_hum_more[row[1]] += 1
                    else:
                        per_wins_hum_more[row[1]] = 1 
            else:
                if(row[6] != ''):
                    curr_temp = min(int(row[5]),int(row[6]))
                else:
                    curr_temp = int(row[5])
                    if(temps[row[3]] > curr_temp):
                        if(row[3] in per_wins_temp_less):
                            per_wins_temp_less[row[3]] += 1
                        else:
                            per_wins_temp_less[row[3]] = 1
                    else:
                        if(row[3] in per_wins_temp_more):
                            per_wins_temp_more[row[3]] += 1
                        else:
                            per_wins_temp_more[row[3]] = 1
                if( row[7] == '' ):
                    curr_humidity = 0
                elif( len(row[7])  == 2 ):
                    curr_humidity= int(row[7][0])
                else:
                    curr_humidity= int(row[7][0:2])        
                if(humidity[row[3]] > curr_humidity):
                    if(row[3] in per_wins_hum_less):
                        per_wins_hum_less[row[3]] += 1
                    else:
                        per_wins_hum_less[row[3]] = 1
                else:
                    if(row[3] in per_wins_hum_more):
                        per_wins_hum_more[row[3]] += 1
                    else:
                        per_wins_hum_more[row[3]] = 1 
            numRow += 1
        else:
            numRow += 1
    # Calculate PER.WINS.TEMP.LESS
    for team in per_wins_temp_less:
        per_wins_temp_less[team] = round( (per_wins_temp_less[team] / per_wins[team])*100 ,2)
    # Calculate PER.WINS.TEMP.MORE
    for team in per_wins_temp_more:
        per_wins_temp_more[team] = round( (per_wins_temp_more[team] / per_wins[team])*100 ,2)
    # Calculate PER.WINS.HUM.LESS
    for team in per_wins_hum_less:
        per_wins_hum_less[team] = round( (per_wins_hum_less[team] / per_wins[team])*100 ,2)
    # Calculate PER.WINS.HUM.MORE
    for team in per_wins_hum_more:
        per_wins_hum_more[team] = round( (per_wins_hum_more[team] / per_wins[team])*100 ,2)
    # Calculate PER.WINS
    for team in per_wins:
        per_wins[team] = round( (per_wins[team] / (games_home[team] + games_away[team]))*100 , 2)

    # IF A TEAM DOES NOT EXIST IN A CATEGORY, ADD IT.
    for team in per_wins:
        if(team not in per_wins_home):
            per_wins_home[team] = 0.00
        if(team not in per_wins_away):
            per_wins_away[team] = 0.00
        if(team not in per_wins_temp_less):
            per_wins_temp_less[team] = 0.00
        if(team not in per_wins_temp_more):
            per_wins_temp_more[team] = 0.00
        if(team not in per_wins_hum_less):
            per_wins_hum_less[team] = 0.00
        if(team not in per_wins_hum_more):
            per_wins_hum_more[team] = 0.00
    # Convert all percents to strings and append %
    for team in per_wins:
        per_wins[team] = str(per_wins[team]) + "%"
        per_wins_home[team] = str(per_wins_home[team]) + "%"
        per_wins_away[team] = str(per_wins_away[team]) + "%"
        per_wins_temp_less[team] = str(per_wins_temp_less[team]) + "%"
        per_wins_temp_more[team] = str(per_wins_temp_more[team]) + "%"
        per_wins_hum_less[team] = str(per_wins_hum_less[team]) + "%"
        per_wins_hum_more[team] = str(per_wins_hum_more[team]) + "%"

    # READY TO OUTPUT
    # AVG.TEMP --> temps
    # AVG.HUM --> humidity
    # PER.WINS --> per_wins
    # PER.WINS.HOME --> per_wins_home
    # PER.WINS.AWAY --> per_wins_away
    # PER.WINS.TEMP.LESS --> per_wins_temp_less
    # PER.WINS.TEMP.MORE --> per_wins_temp_more
    # PER.WINS.HUM.LESS --> per_wins_hum_less
    # PER.WINS.HUM.MORE --> per_wins_hum_more

    # Write all results
    csv_file_output.writerow(output_headers)
    numWritten = 0

    if(len(argv) == 3):
        for team in per_wins:
            row = [team, addDecimals(temps[team]), addDecimals(humidity[team]), per_wins[team], per_wins_home[team], per_wins_away[team], per_wins_temp_less[team], per_wins_temp_more[team], per_wins_hum_less[team], per_wins_hum_more[team]]
            csv_file_output.writerow(row)
    elif(len(argv) == 4):
        for team in per_wins:
            check = team.split(" ")
            if(len(check) == 3):
                temp = [(check[0] + " " + check[1]).lower(), check[2].lower()]
                check = temp
            else:
                check[0] = check[0].lower()
                check[1] = check[1].lower()
            if((argv[3]).lower() in check):
                row = [team, addDecimals(temps[team]), addDecimals(humidity[team]), per_wins[team], per_wins_home[team], per_wins_away[team], per_wins_temp_less[team], per_wins_temp_more[team], per_wins_hum_less[team], per_wins_hum_more[team]]
                csv_file_output.writerow(row)
                numWritten += 1
        if(numWritten == 0):
            print("ERROR: No records for that team/city were found. Output will be blank.") 
            print("Please try again with different input.")

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