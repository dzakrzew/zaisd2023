"""
Algorytm różnicowy (differential evolution)

Autor:  <@student.polsl.pl>
Data: 25-04-2023
"""

import random
from test_functions import sphere_fun

N = 3 # wymiar funkcji
GENERATIONS = 1000 # liczba generacji
POPULATION_SIZE = 20 # rozmiar populacji
MUTATION_RATE = 0.8 # prawdopodobienstwo mutacji
CROSSOVER_RATE = 0.7 # prawdopodobienstwo krzyzowania
FUN_RANGE = [-10, 10] # przedzial funkcji
FUN = sphere_fun # wybrana funkcja

def mutate(target, population):
    indexes = list(range(len(population)))
    indexes.remove(target)
    random_indexes = random.sample(indexes, 3)

    a, b, c = population[random_indexes[0]], population[random_indexes[1]], population[random_indexes[2]]
    mutant = a[:]

    for i in range(len(a)):
        mutant[i] += MUTATION_RATE * (b[i] - c[i])
    
    return mutant

def crossover(target, mutant):
    cross_points = [random.random() < CROSSOVER_RATE for _ in target]
    
    if not any(cross_points):
        cross_points[random.randint(0, len(target) - 1)] = True
    
    offspring = [mutant[i] if cross_points[i] else target[i] for i in range(len(target))]
    return offspring


population = [[random.uniform(FUN_RANGE[0], FUN_RANGE[1]) for i in range(N)] for _ in range(POPULATION_SIZE)]

min_fitness = FUN(population[0])
min_individual = population[0]

for _ in range(GENERATIONS):
    for target_index in range(POPULATION_SIZE):
        target = population[target_index]
        mutant = mutate(target_index, population)
        offspring = crossover(target, mutant)
        offspring_fitness = FUN(offspring)

        if offspring_fitness < FUN(target):
            population[target_index] = offspring

            if offspring_fitness < min_fitness:
                min_fitness = offspring_fitness
                min_individual = offspring
            
print("Najlepszy osobnik: {}".format(min_individual))
print("Wynik f(x) = {}".format(min_fitness))