# Data Science Project 2
# Alessio Mazzone

import csv
import sys
import networkx as nx


def main(argv):

    # python3 compute_active.py graph.csv   px     results.csv
    #                 argv[0]    argv[1]  argv[2]    argv[3]
    #                            graph   probability

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

    #traversal = list(nx.edge_dfs(nx.DiGraph(edges), 1))
    #print(traversal)

    for node in nodes:
        traversals.append(list(nx.edge_dfs(nx.DiGraph(edges), node)))

        # Initialize list of activations. 
        # Each node is counted a minimum of once.
        num_activations[node] = 1

    # Curr node we are on
    i = 0
    for traversal in traversals:
        if(len(traversal) != 0):
            for edge in traversal:
                if (edge[1] % px == 0 and edge[1] not in visited):
                    visited.append(edge[1])
                    num_activations[nodes[i]] += 1
            # Increment node        
            i += 1
            visited = []


    for key in num_activations.keys():
        print(key, ",", num_activations[key])
 
    # Close files at end
    csv_raw_input.close() 
    csv_raw_output.close() 


if __name__ == "__main__":

        #print(traversal)
    main(sys.argv)