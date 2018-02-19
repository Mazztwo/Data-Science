# CS 1656 
# Data Science 
# Project 2
# Alessio Mazzone

import csv
import sys
import networkx as nx


def main(argv):

    # Open CSV input file in read mode
    # Open CSV output file in write mode, overwrite if already exists
    csv_raw_input = open(argv[1], newline='')
    csv_raw_output = open(argv[3], "w")


    # Create CSV objects with raw files
    csv_file_input = csv.reader(csv_raw_input)
    csv_file_output = csv.writer(csv_raw_output)

    # Create our directed graph
    directedGraph = nx.DiGraph()

    # Create lists
    nodes = []
    edges = []
    traversals = []
    num_activations = {}
    px = int(argv[2])
    visited = []
    activated = []


    # Read csv and create graph
    for row in csv_file_input:

        node1 = int(row[0])
        node2 = int(row[1])

        # Add nodes to list of nodes
        if(node1 not in nodes):
            nodes.append(node1)
        if(node2 not in nodes):
            nodes.append(node2)

        edges.append((node1,node2))
    
    # sort list of nodes
    nodes = sorted(nodes)

    for node in nodes:
        traversals.append(list(nx.edge_dfs(nx.DiGraph(edges), node)))

        # Initialize list of activations. 
        # Each node is counted a minimum of once.
        num_activations[node] = 1

    # Curr node we are on
    i = 0
    for traversal in traversals:
        if(len(traversal) != 0):
            # Add start node to activated list
            activated.append(i + 1)
            for edge in traversal:
                if (edge[1] % px == 0): 
                    visited.append(edge[1])
                    # Only activate node if edge[0] is activated..
                    if(edge[0] in activated and edge[1] not in activated):
                        num_activations[nodes[i]] += 1
                        activated.append(edge[1])

        # Increment node        
        i += 1
        # Clear visited nodes
        visited = []
        # Clear activated nodes
        activated = []

    output = []

    # Convert dictionary to list of touples
    for key in num_activations.keys():
        output.append((key, num_activations[key]))       

    # Sort list of touples by number of activations
    sortedOutput = sorted(output, key=lambda tup: tup[1])[::-1]

    # Sort by smallest nodeID if ties occur
    for i in range(0, len(sortedOutput)):
        if(i+1 < len(sortedOutput)):
            if(sortedOutput[i][1] == sortedOutput[i+1][1]):
                if(sortedOutput[i][0] > sortedOutput[i+1][0]):
                    temp = sortedOutput[i]
                    sortedOutput[i] = sortedOutput[i+1]
                    sortedOutput[i+1] = temp

    # Print to output
    for pair in sortedOutput:
        csv_file_output.writerow( str(pair[0]) + str(pair[1]) )
 
    # Close files at end
    csv_raw_input.close() 
    csv_raw_output.close() 


if __name__ == "__main__":
    main(sys.argv)