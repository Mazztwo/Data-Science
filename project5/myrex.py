#   Alessio Mazzone       #
#   CS 1656 Data Science  #
#   Project 5             #
###########################

import sys


def main(argv):

    command = argv[1]


    if(command == "predict"):
        print("Predict!")

    elif(command == "evaluate"):
        print("Evaluate!")
    else:
        print("ERROR: '%s' is not an accepted argument." %(command))





if __name__ == "__main__":
    main(sys.argv)
