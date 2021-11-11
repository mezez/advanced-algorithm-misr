import numpy as np
import copy
import math
np.random.seed(0)

def compute():
    iterations = 3
    cost_matrix = np.array([[0, 10, 12, 11, 14]
              , [10, 0, 13, 15, 8]
              , [12, 13, 0, 9, 14]
              , [11, 15, 9, 0, 16]
              , [14, 8, 14, 16, 0]])
    size = len(cost_matrix)
    number_of_couples = math.floor(size/4)
    number_of_winners_to_keep = 2
    cities= generateCities(size)
    chromosomes=createStartingGeneration(size, cities)
    best = None
    for i in range(0,iterations):
        new_chromosomes = []
        scores = chromosomesFitness(chromosomes, cost_matrix)
        print(scores)
        best = chromosomes[np.argmin(scores)]
        distance = fitness(size, best, cost_matrix)
        for j in range(0, number_of_couples):  
            new_1, new_2 = crossover(chromosomes[breedChromosomes(scores)], chromosomes[breedChromosomes(scores)])
            new_chromosomes = np.array([new_1, new_2])
        for j in range(0, len(new_chromosomes)):
              new_chromosomes[j] = np.copy(mutate(new_chromosomes[j], size, 0.05))
        new_chromosomes = np.append(new_chromosomes,[chromosomes[np.argmin(scores)]],axis=0)
        for j in range(1, number_of_winners_to_keep):
           keeper = breedChromosomes(scores)            
           new_chromosomes = np.append(new_chromosomes, [chromosomes[keeper]], axis= 0)
        # add new random members
        while len(new_chromosomes) < size:
            new_chromosomes = np.append(new_chromosomes, [createNewChromosome(cities)], axis=0)
        chromosomes = np.array(copy.deepcopy(new_chromosomes))
    print(distance, best)

#Calculates the distance traveled by chromosome.
def fitness(size, chromosome, cost_matrix):
    score = 0
    for i in range(size-1):
        score += cost_matrix[chromosome[i]-1, chromosome[i+1]-1]
    return score

#Mix 2 different solutions and create a new one
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
    mutated_chromosome=chromosome
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

# creates a certane ammount of chromosomes
def createNexGeneration(population):
    return population

# creates a certane ammount of starting chromosomes
def createStartingGeneration(size, cities):
    chromosomes = []
    for i in range(size):
        chromosomes.append(createNewChromosome(cities))
    return(np.array(chromosomes))
#Calculates score of each chromosome in population
def chromosomesFitness(chromosomes, cost_matrix):
    scores = []
    for i in range(len(chromosomes)):
        scores.append(fitness(len(chromosomes[i]) ,chromosomes[i], cost_matrix))
    return scores
#Breed chromosomes
def breedChromosomes(scores):
    array = np.array(scores)
    temp = array.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(array))

    fitness = [len(ranks) - x for x in ranks]
    
    cum_scores = copy.deepcopy(fitness)
    
    for i in range(1,len(cum_scores)):
        cum_scores[i] = fitness[i] + cum_scores[i-1]
        
    probs = [x / cum_scores[-1] for x in cum_scores]
    
    rand = np.random.random()
    
    for i in range(0, len(probs)):
        if rand < probs[i]:
            
            return i
#generate indexes of cities from matrix
def generateCities(size):
    cities= []
    for i in range(size):
        cities.append(i+1)
    return np.array(cities)
        