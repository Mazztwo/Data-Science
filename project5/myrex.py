#   Alessio Mazzone       #
#   CS 1656 Data Science  #
#   Project 5             #
###########################

import sys






def predict():
    print("Predict!")
    
    # Parse command line args
    trainingFile = argv[2]
    k = argv[3]
    algorithm = argv[4]
    userID = argv[5]
    movieID = argv[6]

def evaluate():
    print("Evaluate!")

    # Parse command line args
    trainingFile = argv[2]
    k = argv[3]
    algorithm = argv[4]
    testingFile = argv[5]


def main(argv):



    if(argv[1] == "predict"):
        predict()
    elif(argv[1] == "evaluate"):
        evaluate()
    else:
        print("ERROR: '%s' is not an accepted argument." %(argv[1]))

if __name__ == "__main__":
    main(sys.argv)
