import numpy as np
import copy
import math
from utils import read_tsp_file
np.random.seed(0)


def geneticApproach(uploaded_file):
    iterations = 1000
    cost_matrix = np.array(read_tsp_file(uploaded_file)[0])
    size = len(cost_matrix)
    number_of_couples = math.floor(size/4)
    number_of_winners_to_keep = 2
    cities = generateCities(size)
    chromosomes = createStartingGeneration(size, cities)
    best = None
    for i in range(0, iterations):
        new_chromosomes = []
        scores = chromosomesFitness(chromosomes, cost_matrix)
        best = chromosomes[np.argmin(scores)]
        distance = fitness(size, best, cost_matrix)
        # Mix already existing chromosomes
        for j in range(0, number_of_couples):
            new_1, new_2 = crossover(chromosomes[breedChromosomes(
                scores)], chromosomes[breedChromosomes(scores)])
            new_chromosomes = np.array([new_1, new_2])
        # Mutate chromosomes, reorder nodes from random location
        for j in range(0, len(new_chromosomes)):
            new_chromosomes[j] = np.copy(
                mutate(new_chromosomes[j], size, 0.05))
        new_chromosomes = np.append(
            new_chromosomes, [chromosomes[np.argmin(scores)]], axis=0)
        # Keep the best chromosomes from the previous generation
        for j in range(1, number_of_winners_to_keep):
            keeper = breedChromosomes(scores)
            new_chromosomes = np.append(
                new_chromosomes, [chromosomes[keeper]], axis=0)
        # Add new random members
        while len(new_chromosomes) < size:
            new_chromosomes = np.append(
                new_chromosomes, [createNewChromosome(cities)], axis=0)
        chromosomes = np.array(copy.deepcopy(new_chromosomes))
    distance += cost_matrix[best[len(best)-1]-1, best[0]-1]
    best = np.append(best, best[0])
    return([int(distance), best, cost_matrix])


# Calculates the distance traveled by chromosome.
def fitness(size, chromosome, cost_matrix):
    score = 0
    for i in range(size-1):
        score += cost_matrix[chromosome[i]-1, chromosome[i+1]-1]
    return score


# Mix 2 different solutions and create a new one
def crossover(a, b):
    cut = np.random.randint(1, len(a)-1)
    new_a1 = copy.deepcopy(np.random.permutation(a[0:cut]))
    new_a2 = copy.deepcopy(a[cut:])
    new_b1 = copy.deepcopy(np.random.permutation(b[0:cut]))
    new_b2 = copy.deepcopy(b[cut:])
    new_a = np.append(new_a1, new_a2)
    new_b = np.append(new_b1, new_b2)

    return (new_a, new_b)


# Add random noice inside of results
def mutate(chromosome, size, probability):
    mutated_chromosome = chromosome
    for i in range(len(chromosome)):
        if np.random.random() < probability:
            a = chromosome[0:i]
            b = np.random.permutation(chromosome[i:size])
            mutated_chromosome = np.array([*a, *b])
            break
    return mutated_chromosome


# Creates a random chromosome
def createNewChromosome(cities):
    return (np.array(np.random.permutation(cities)))


# Creates a certane ammount of chromosomes
def createNexGeneration(population):
    return population


# Creates a certane ammount of starting chromosomes
def createStartingGeneration(size, cities):
    chromosomes = []
    for i in range(size):
        chromosomes.append(createNewChromosome(cities))
    return(np.array(chromosomes))


# Calculates score of each chromosome in population
def chromosomesFitness(chromosomes, cost_matrix):
    scores = []
    for i in range(len(chromosomes)):
        scores.append(
            fitness(len(chromosomes[i]), chromosomes[i], cost_matrix))
    return scores


# Breed chromosomes
def breedChromosomes(scores):
    array = np.array(scores)
    temp = array.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(array))
    fitness = [len(ranks) - x for x in ranks]
    cum_scores = copy.deepcopy(fitness)
    for i in range(1, len(cum_scores)):
        cum_scores[i] = fitness[i] + cum_scores[i-1]
    probs = [x / cum_scores[-1] for x in cum_scores]
    rand = np.random.random()
    for i in range(0, len(probs)):
        if rand < probs[i]:
            return i


# Generate indexes of cities from matrix
def generateCities(size):
    cities = []
    for i in range(size):
        cities.append(i+1)
    return np.array(cities)

# References:
# https://jaketae.github.io/study/genetic-algorithm/
# https://www.youtube.com/watch?v=uCXm6avugCo
