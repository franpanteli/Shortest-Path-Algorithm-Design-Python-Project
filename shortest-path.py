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
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'A','F')