"""
Algorytm genetyczny (genetic algorithm)

Autor:  <@student.polsl.pl>
Data: 04-05-2023
"""

import random
from test_functions import sphere_fun

N = 3 # wymiar funkcji
POPULATION_SIZE = 20 # rozmiar populacji
MUTATION_RATE = 0.3 # prawdopodobienstwo mutacji
CROSSOVER_RATE = 1 # prawdopodobienstwo krzyzowania
GENERATIONS = 1000 # liczba generacji
FUN_RANGE = [-10, 10] # przedzial funkcji
FUN = sphere_fun # wybrana funkcja

class Individual:
    def __init__(self):
        self.x = [random.uniform(FUN_RANGE[0], FUN_RANGE[1]) for _ in range(N)]
    
    def __str__(self):
        return "Individual ({}) fitness: {}".format(str(self.x), self.get_fitness())
    
    def __repr__(self):
        return "Individual ({}) fitness: {}".format(str(self.x), self.get_fitness())
    
    def mutate(self):
        for i in range(N):
            l = random.uniform(0, 1)
            if l < MUTATION_RATE:
                ksi = random.uniform(-0.5, 0.5)
                self.x[i] += ksi
    
    def get_fitness(self):
        return 1000 - FUN(self.x)


def crossover(parent1, parent2):
    r = random.uniform(0, 1)

    # nowe osobniki
    offspring1, offspring2 = Individual(), Individual()

    for j in range(N):
        offspring1.x[j] = parent1.x[j] + (r * parent2.x[j])
        offspring2.x[j] = parent2.x[j] + (r * parent1.x[j])

    return offspring1, offspring2

# wybór do reprodukcji/mutacji na podstawie prawdopodobieństwa zależącego od funkcji kryterialnej
def choose_to_reproduce(population, alpha):
    s = sum([_.get_fitness() for _ in population])
    st = 0
    i = 0

    for individual in population:
        st += individual.get_fitness() / s
        
        if alpha <= st:
            break
        
        i += 1

    return i

def reproduce(population, new_population = []):
    # Wybór osobników do reprodukcji wg prawdopodobieństwo (Pr)
    alpha, beta = random.uniform(0, 1), random.uniform(0, 1)
    i1, i2 = choose_to_reproduce(population, alpha), choose_to_reproduce(population, beta)

    # Mutacja
    population[i1].mutate()
    population[i2].mutate()

    # Krzyżowanie
    offspring1, offspring2 = crossover(population[i1], population[i2])

    # Wybór wygranych
    if offspring1.get_fitness() > population[i1].get_fitness():
        new_population.append(offspring1)
    else:
        new_population.append(population[i1])

    if offspring2.get_fitness() > population[i2].get_fitness():
        new_population.append(offspring2)
    else:
        new_population.append(population[i2])

    if len(new_population) < POPULATION_SIZE:
        reproduce(population, new_population)
    
    return new_population

# Inicjalizacja losowej populacji
pop = [Individual() for _ in range(POPULATION_SIZE)]

# Iteracje wg liczby generacji
for _ in range(GENERATIONS):
    pop = reproduce(pop)

# Wybór najlepszego osobnika
best_individual = max(pop, key=lambda i: i.get_fitness())

print("Najlepszy osobnik: {}".format(best_individual))
print("Wynik f(x) = {}".format(FUN(best_individual.x)))