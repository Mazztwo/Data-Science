# Data Science Project 2
# Alessio Mazzone

import csv
import sys
import networkx as nx

# REMOVE BEFORE TURNING IN!!!
import matplotlib.pyplot as plt
###############################


def main(argv):

    # python3 compute_active.py graph.csv   px     results.csv
    #                 argv[0]    argv[1]  argv[2]    argv[3]
    #                            graph   probability

    # Open CSV input file in read mode
    # Open CSV output file in write mode, overwrite if already exists
    csv_raw_input = open(argv[1], newline='')
    #csv_raw_output = open(argv[3], "w")


    # Create CSV objects with raw files
    csv_file_input = csv.reader(csv_raw_input)
    #csv_file_output = csv.writer(csv_raw_output)

    # Create our directed graph
    graph = nx.DiGraph()

    # Create list of nodes
    nodes = []

    # Read csv and create graph
    for row in csv_file_input:

        # Add edge to graph
        graph.add_edge(row[0],row[1])
        node1 = int(row[0])
        node2 = int(row[1])

        # Add nodes to list of nodes
        if(node1 not in nodes):
            nodes.append(node1)
        if(node2 not in nodes):
            nodes.append(node2)
    
    # sort list of nodes
    nodes = sorted(nodes)

    # REMOVE BEFORE TURNING IN!!!
    nx.draw(graph, with_labels=True)
    plt.show()
    ###############################

    #list(edge_dfs(graph, nodes))


    print(nodes)


    # Close files at end
    csv_raw_input.close() 
    #csv_raw_output.close() 


if __name__ == "__main__":
    main(sys.argv)