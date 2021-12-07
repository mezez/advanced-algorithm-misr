import sys
from utils import read_tsp_file


#  Function to find the minimum
#  cost path for all the paths
def findMinRoute(cost_matrix):
    sum = 0
    counter = 0
    j = 0
    i = 0
    min = sys.maxsize
    visited_route_list = []
    #  Starting from the 0th indexed
    #  city i.e., the first city
    visited_route_list.append(0)
    route = [0] * (len(cost_matrix))
    #  Traverse the adjacency
    #  matrix tsp[][]
    while (i < len(cost_matrix) and j < len(cost_matrix[i])):
        #  Corner of the Matrix
        if (counter >= len(cost_matrix[i]) - 1):
            break
        #  If this path is unvisited then
        #  and if the cost is less then
        #  update the cost
        if (j != i and not (j in visited_route_list)):
            if (cost_matrix[i][j] < min):
                min = cost_matrix[i][j]
                route[counter] = j + 1
        j += 1
        #  Check all paths from the
        #  ith indexed city
        if (j == len(cost_matrix[i])):
            sum += min
            min = sys.maxsize
            visited_route_list.append(route[counter] - 1)
            j = 0
            i = route[counter] - 1
            counter += 1
    #  Update the ending city in list
    #  from city which was last visited
    i = route[counter - 1] - 1
    j = 0
    while (j < len(cost_matrix)):
        if ((i != j) and cost_matrix[i][j] < min):
            min = cost_matrix[i][j]
            route[counter] = j + 1
        j += 1
    sum += min
    #  Started from the node where
    #  we finished as well.
    visited_route_list.append(0)
    for i in range(len(visited_route_list)):
        visited_route_list[i] = visited_route_list[i]+1
    return [int(sum), visited_route_list, cost_matrix]


def compute(filename):
    #  Input Matrix
    dist_mat = read_tsp_file(filename)[0]
    response = findMinRoute(dist_mat)
    return [response[0], response[1], dist_mat]


#  Driver Code
def main(self, args):
    #  Input Matrix
    tsp = [[-1, 10, 15, 20], [10, -1, 35, 25],
           [15, 35, -1, 30], [20, 25, 30, -1]]
    #  Function Call
    self.findMinRoute(tsp)

# reference
# https://www.geeksforgeeks.org/travelling-salesman-problem-greedy-approach/
