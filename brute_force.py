import numpy as np
from itertools import permutations
from utils import read_tsp_file


def brute_force(uploaded_file):

    matrix = read_tsp_file(uploaded_file)
    start_city = 0
    distance_matrix = np.array(matrix[0])
    number_of_cities = len(distance_matrix)

    cities = [city_index for city_index in range(0, number_of_cities)]
    all_paths = list(permutations(cities[1:]))
    all_travels = []

    for path in all_paths:
        travel = list(path)
        travel.insert(0, 0)
        cost = 0

        for index, node in enumerate(travel):
            if index == len(travel) - 1:
                cost = cost + distance_matrix[node][0]
            else:
                cost = cost + distance_matrix[node][travel[index+1]]

        all_travels.append((cost, travel))

    optimal_path = min(all_travels)
    optimal_path[1].append(start_city)
    return [int(optimal_path[0]), str(optimal_path[1]), distance_matrix]
