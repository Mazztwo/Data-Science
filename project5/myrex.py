#   Alessio Mazzone       #
#   CS 1656 Data Science  #
#   Project 5             #
###########################

import sys
import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean, cityblock, cosine
from scipy.stats import pearsonr

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
    print("Predict!")
    
    # Make globals accessible
    global trainingFile
    global k
    global algorithm
    global userID
    global movieID

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

    printOutput()


def evaluate(argv):
    print("Evaluate!")

    # Make globals accessible
    global trainingFile
    global k
    global algorithm
    global testingFile

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
