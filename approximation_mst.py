import numpy as np
from branch_and_bound import read_tsp_file


def approximationMST(uploaded_file):
    starting_node = 1
    path = [starting_node]
    distance = 0
    cost_matrix = np.array(read_tsp_file(uploaded_file)[0])
    distance, route = (minimumSpanningTree(
        cost_matrix, starting_node, path, distance))
    distance += cost_matrix[route[len(route)-1]-1, starting_node-1]
    route = np.append(route, route[starting_node-1])
    return([int(distance), str(route), cost_matrix])


def minimumSpanningTree(cost_matrix, starting_node=1, path=[1], distance=0):
    route = np.array(path)
    current_distance = distance
    min_dist = np.inf
    min_dist_node = None
    for i in range(len(cost_matrix[starting_node-1])):
        if cost_matrix[starting_node-1, i] < min_dist and not np.isin(i+1, route):
            min_dist = cost_matrix[starting_node-1, i]
            min_dist_node = i+1
    route = np.append(route, min_dist_node)
    current_distance += min_dist
    if(len(route) >= len(cost_matrix)):
        return (current_distance, route)
    else:
        return minimumSpanningTree(cost_matrix, min_dist_node, route, current_distance)
