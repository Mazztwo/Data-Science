#   Alessio Mazzone       #
#   CS 1656 Data Science  #
#   Project 5             #
###########################

import sys
import pandas
from scipy.stats import pearsonr
import numpy as np
from scipy.spatial.distance import euclidean, cosine

# Make variables accessible to all functions
command = ""
trainingFile = ""
k = 0
algorithm = ""
userID = 0
movieID = 0
testingFile = ""
prediction = 0

def predict(argv):
    
    # Make globals accessible
    global trainingFile
    global k
    global algorithm
    global userID
    global movieID
    global prediction

    # Parse command line args
    trainingFile = argv[2]
    k = int(argv[3])
    algorithm = argv[4]
    userID = int(argv[5])
    movieID = int(argv[6])

    # Error checking!
    #################
    # userID
    # movieID
    # training file unreadable
    # wrong algorithm
    # k not positive integer
    if(isinstance(userID, int) == False or userID < 1):
        print("ERROR: userID is invalid.")
        sys.exit()
    elif(isinstance(movieID, int) == False or movieID < 1):
        print("ERROR: movieID is invalid.")
        sys.exit()
    elif(isinstance(k, int) == False < 1):
        print("ERROR: k is ivalid.")
        sys.exit()
   


    #Training file structure:
    # userID | movieID | rating | timestamp
    # userID/movieID start: 1

    if(algorithm == "average"):
        average()
    elif(algorithm == "euclid"):
        euclid()
    elif(algorithm == "pearson"):
        pearson()
    elif(algorithm == "cosine"):
        cosn()
    else:
        print("ERROR: algorithm is invalid.")
        sys.exit()  

    

    printOutput()

def evaluate(argv):

    # Make globals accessible
    global trainingFile
    global k
    global algorithm
    global testingFile
    global prediction

    # Parse command line args
    trainingFile = argv[2]
    k = int(argv[3])
    algorithm = argv[4]
    testingFile = argv[5]


    # Error checking!
    #################
    # training or testing files unreadable
    # wrong algorithm
    # k not positive integer
    if(isinstance(k, int) == False < 1):
        print("ERROR: k is ivalid.")
        return -1
    elif(algorithm != "average" and algorithm != "euclid" and algorithm != "pearson" and algorithm != "cosine"):
        print("ERROR: algorithm is invalid.")
        return -1

    try:
        with open(trainingFile) as file:
            for row in file:
                info = row.split()
    except EnvironmentError:
        print("ERROR: Training file could not be opened.")
        return -1

    try:
        with open(testingFile) as file:
            for row in file:
                info = row.split()
    except EnvironmentError:
        print("ERROR: Testing file could not be opened.")
        return -1


    # Training file structure:
    # userID | movieID | rating | timestamp
    # userID/movieID start: 1

    printOutput()

def printOutput():

    global command
    global algorithm
    global trainingFile
    global k
    global userID
    global movieID
    global prediction

    print("myrex.command      =  %s" % (command)) 
    print("myrex.training     =  %s" % (trainingFile)) 
    print("myrex.algorithm    =  %s" % (algorithm)) 
    print("myrex.k            =  %d" % (k)) 
    print("myrex.userID       =  %d" % (userID)) 
    print("myrex.movieID      =  %d" % (movieID)) 
    print("myrex.prediction   =  %f" % (prediction)) 

def average():

    global trainingFile
    global prediction

    try:
        with open(trainingFile) as file:
            
            count = 0
            total = 0

            for row in file:
                info = [int(n) for n in row.split()]
                    
                if(info[1] == movieID):
                    count += 1
                    total += info[2]

            prediction = float(total) / float(count)

    except EnvironmentError:
        print("ERROR: Training file could not be opened.")
        sys.exit()

def euclid():
    
    global trainingFile
    global prediction
    global k
    global userID
    global movieID

    userRatings = {}
    tempUserRatings = {}
    sim_weights = {}
    ratings1 = []
    ratings2 = []
    weightsSum = 0.0

    # Make sure file exists
    try:
        with open(trainingFile) as file:
            pass
    except EnvironmentError:
        print("ERROR: Training file could not be opened.")
        sys.exit()

    column_names = ['userID', 'movieId', 'rating', 'timestamp']
    dataFile = pandas.read_table(trainingFile, delimiter = '\t', names = column_names)

    for row in dataFile[dataFile['userID'] == userID].itertuples():
        #           |movieID|rating|
        userRatings[row[2]] = row[3]

    # Compute weighted similarities
    for user in dataFile["userID"].unique():
        if(user != userID):
            # get shared ratings
            for row in dataFile[dataFile['userID'] == user].itertuples():
                if(row[2] in userRatings):
                    ratings2.append(row[3])   
                    ratings1.append(userRatings[row[2]])   
        else:
            continue
        
        dist = euclidean(ratings1, ratings2)
        sim_weights[user] = 1.0 / (1.0 + dist)    

    # Now compare to k nearest neighbors
    if(k == 0): # compare to all
        for user in dataFile["userID"].unique():
            if(user != userID):
                for row in dataFile[dataFile['userID'] == user].itertuples():
                    if(row[2] == movieID):
                        prediction += row[3] * sim_weights[user]
                        weightsSum += sim_weights[user]
    else:
        count = 0
        sorted_weights = sorted(sim_weights.items(), key = lambda pair: pair[1], reverse=True)

        for user, weight in sorted_weights:
            if(count >= k):
                break
            if(user != userID):
                for row in dataFile[dataFile['userID'] == user].itertuples():
                    if(row[2] == movieID):
                        prediction += row[3] * sim_weights[user]
                        weightsSum += sim_weights[user]
                        count += 1

            

    prediction /= weightsSum

def pearson():
    global trainingFile
    global prediction
    global k
    global userID
    global movieID

    userRatings = {}
    tempUserRatings = {}
    sim_weights = {}
    ratings1 = []
    ratings2 = []
    weightsSum = 0.0

    # Make sure file exists
    try:
        with open(trainingFile) as file:
            pass
    except EnvironmentError:
        print("ERROR: Training file could not be opened.")
        sys.exit()

    column_names = ['userID', 'movieId', 'rating', 'timestamp']
    dataFile = pandas.read_table(trainingFile, delimiter = '\t', names = column_names)

    for row in dataFile[dataFile['userID'] == userID].itertuples():
        #           |movieID|rating|
        userRatings[row[2]] = row[3]

    # Compute weighted similarities
    for user in dataFile["userID"].unique():
        if(user != userID):
            # get shared ratings
            for row in dataFile[dataFile['userID'] == user].itertuples():
                if(row[2] in userRatings):
                    ratings2.append(row[3])   
                    ratings1.append(userRatings[row[2]])   
        else:
            continue
        
        dist = pearsonr(ratings1, ratings2)[0]
        sim_weights[user] = dist   

    # Now compare to k nearest neighbors
    if(k == 0): # compare to all
        for user in dataFile["userID"].unique():
            if(user != userID):
                for row in dataFile[dataFile['userID'] == user].itertuples():
                    if(row[2] == movieID):
                        normRating = (2.0 * (row[3] - 1.0) - 4.0) * 0.25
                        prediction += normRating * sim_weights[user]
                        weightsSum += sim_weights[user]
    else:
        count = 0
        sorted_weights = sorted(sim_weights.items(), key = lambda pair: pair[1], reverse=True)

        for user, weight in sorted_weights:
            if(count >= k):
                break
            if(user != userID):
                for row in dataFile[dataFile['userID'] == user].itertuples():
                    if(row[2] == movieID):
                        normRating = (2.0 * (row[3] - 1.0) - 4.0) * 0.25
                        prediction += normRating * sim_weights[user]
                        weightsSum += abs(sim_weights[user])
                        count += 1

            

    prediction /= weightsSum

    prediction = 1 + (((prediction + 1.0) * 4) / (2.0))

def cosn():
    global trainingFile
    global prediction
    global k
    global userID
    global movieID

    userRatings = {}
    tempUserRatings = {}
    sim_weights = {}
    ratings1 = []
    ratings2 = []
    weightsSum = 0.0

    # Make sure file exists
    try:
        with open(trainingFile) as file:
            pass
    except EnvironmentError:
        print("ERROR: Training file could not be opened.")
        sys.exit()

    column_names = ['userID', 'movieId', 'rating', 'timestamp']
    dataFile = pandas.read_table(trainingFile, delimiter = '\t', names = column_names)

    for row in dataFile[dataFile['userID'] == userID].itertuples():
        #           |movieID|rating|
        userRatings[row[2]] = row[3]

    # Compute weighted similarities
    for user in dataFile["userID"].unique():
        if(user != userID):
            # get shared ratings
            for row in dataFile[dataFile['userID'] == user].itertuples():
                if(row[2] in userRatings):
                    ratings2.append(row[3])   
                    ratings1.append(userRatings[row[2]])   
        else:
            continue
        
        dist = cosine(ratings1, ratings2)    
        sim_weights[user] = dist
        
    # Now compare to k nearest neighbors
    if(k == 0): # compare to all
        for user in dataFile["userID"].unique():
            if(user != userID):
                for row in dataFile[dataFile['userID'] == user].itertuples():
                    if(row[2] == movieID):
                        prediction += row[3] * sim_weights[user]
                        weightsSum += sim_weights[user]
    else:
        count = 0
        sorted_weights = sorted(sim_weights.items(), key = lambda pair: pair[1], reverse=True)

        for user, weight in sorted_weights:
            if(count >= k):
                break
            if(user != userID):
                for row in dataFile[dataFile['userID'] == user].itertuples():
                    if(row[2] == movieID):
                        prediction += row[3] * sim_weights[user]
                        weightsSum += sim_weights[user]
                        count += 1

            

    prediction /= weightsSum




def main(argv):

    global command

    command = argv[1]

    if(command == "predict"):
        predict(argv)
    elif(command == "evaluate"):
        evaluate(argv)
    else:
        print("ERROR: '%s' is not an accepted argument." %(argv[1]))

if __name__ == "__main__":
    main(sys.argv)
