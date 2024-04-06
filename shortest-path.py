"""
    Defining the graph:
        -> This is the dictionary that stores the graph 
        -> It's in a variable called my_graph
        -> The numbers in this represent the distances from that node in the graph to other nodes in the graph <- weights 
"""

my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

"""
    Defining a function that calculates the shortest path between nodes in the graph:
        -> The arguments of this are:
            -> The graph (the dictionary which stores the graph)
            -> The start node on the graph 
            -> The node we want to calculate the distance to 

        -> Then we are initialising the values of the different variables:
            -> The nodes on the graph which we haven't visited <- we are taking the graph which is stored in a dictionary 
                called `graph` and converting it into a list 

            -> distances:
                -> This is a dictionary which contains the currently stored distance between the source node and every 
                    other node in the graph 
                -> It uses a turnery operator to do this
                -> We are initialising the distance between the starting node on the graph and itself as equal to 0
                -> Then we are initialising the distance between the start node and all other nodes as infinite <- seeing 
                    as we haven't calculated this yet 

            -> paths:
                -> This variable contains a dictionary 
                -> We are going from the current node and calculating the shortest path between it and every other node in 
                    the graph 
                -> This is the dictionary which stores those paths <- rather than the distances, which was the previous variable 
                    initialised 
                -> We are saying, take this current node - store the shortest path to get from it to every other node in the graph 
                    in this dictionary 
                -> This is the dictionary which we are initialising for that 
                -> All of those lists are empty, and there is one of them to get from the current node to each of the other nodes 
                    in the graph 
                -> So that variable which we've initialised is empty, and is to contain the shortest path between the current node 
                    and every other node 
                -> We set the first element of each of those paths equal to the start node, using the .append method 

            -> Then we need to populate the elements which we just initialised 
"""

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
"""
    This section of the code applies Dijkstra's algorithm: 
        -> This is for the shortest path between a selected node in the graph and its other nodes 
        -> We are using the algorithm on this graph because it is for weighted graphs, with non-negative edge weights 
        
    The while loop this block contains:
        -> We are looping through all of the nodes in the graph and visiting them
        -> And carrying on looping until we have finished going through all of the nodes left 
        -> If we are on a current node, then we are choosing the next node of minimum distance - based on where we are in the 
            graph
        -> Look at the nodes that we haven't visited yet, and of those take the one with the shortest distance to the one which 
            we are currently on 

    Performing scans:
        -> We are at a node 
        -> We are then looking at each of the nodes which are connected to that
        -> We have a few different routes which we could go down, given the current node we are at 
        -> If a potential route has a shorter overall weight than the one which is stored as the route with the currently 
            known shortest distance, we need to update it
        -> So we are comparing the potential next routes to go down with the currently known shortest path, and updating the 
            values we have 
        -> There is a case where we end up looping back to the source node, in which case we coppy the path to avoid shared 
            references between nodes 
        -> When we find the path with the shortest distance, we are deleting the one which was previously stored as it, and
            replacing it with this new one
        -> We loop through all of the different nodes with this while loop, and determine the shortest path from the source 
            node to the end node 
        -> The `distances` dictionary then contains the shortest distances from the starting node to the others 
        -> The `paths` dictionary also then contains the shortest paths from the starting node to the others 
"""

    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)
    
"""
    Performing the algorithm multiple times in the same function:
        -> The previous while loop was running the function, but for a source loop to one of the nodes in the graph 
        -> `targets_to_print`
            -> The algorithm is taking a source node and a target node on the graph and calculating the shortest distance 
                between them 
            -> We have a source node
            -> The user can then specify what the target node will be <- if we want to get from the source node to one node 
            -> If they don't specify this target node, then the function will execute the algorithm between the start (source) 
                node and all nodes in the graph 
            -> This variable contains an array for all of the target nodes in the graph which we want to execute the algorithm 
                for
        -> So we have a while loop, which executes the shortest path algorithm from the source node to a target node
        -> We also have a list of target nodes we want to execute this for 
        -> We are now taking this list of target nodes and executing the algorithm on them 
        -> So we are executing it multiple times
        -> Each time we do this, we are calculating the shortest distance between a source node and the target node
        -> This returns the shortest distance between the source and target node, and the path 
        -> That, times the number of different target nodes which we are processing  
"""

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

"""
Return statements:
	-> We then return two dictionaries as part of this 
	-> These contain the shortest paths and distances from the starting node to all other nodes in the graphs
	-> Or from the starting node to the specified target nodes as part of this
"""

    return distances, paths

# Test the function we just defined on the graph stored in the variable at the start of this .py file
shortest_path(my_graph, 'A','F')