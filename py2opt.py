from pyTwoOpt.routfinder import RouteFinder
from branch_and_bound import read_tsp_file


def compute(filename):
    dist_mat = read_tsp_file(filename)[0]
    cities_names = range(len(dist_mat))
    route_finder = RouteFinder(dist_mat, cities_names, iterations=5)
    best_distance, best_route = route_finder.solve()
    best_route.append(0)
    for i in range(len(best_route)):
        best_route[i] = best_route[i]+1
    return [int(best_distance), best_route, dist_mat]


# This code is contributed by Pedram Ataee
# Build upon by Sara Assefa Alemayehu

# reference
# https://github.com/pdrm83/py2opt
