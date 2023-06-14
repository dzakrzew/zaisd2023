"""
Algorytm pszczeli (bee algorithm)

Autor:  <@student.polsl.pl>
Data: 13-04-2023
"""

import random
from test_functions import sphere_fun

N = 3 # wymiar funkcji
GENERATIONS = 1000 # liczba generacji
POPULATION_SIZE = 50 # rozmiar populacji
POP1 = 20 # liczba pszczół wyszukujących
POP2 = 10 # liczba pszczół rekrutujących
FUN = sphere_fun # wybrana funkcja
FUN_RANGE = [-10, 10] # przedzial funkcji

def generate_bees(n):
    return [[random.uniform(FUN_RANGE[0], FUN_RANGE[1]) for i in range(N)] for _ in range(n)]

def search_bees():
    return generate_bees(POP1)

def recruit_bees(bees, best_bee):
    return [list(best_bee) for _ in range(POP2)] + generate_bees(len(bees) - POP2)

def local_search(bees):
    for bee in bees:
        dimension_to_modify = random.randint(0, len(bee) - 1)
        bee[dimension_to_modify] += random.uniform(-1, 1)


bees = generate_bees(POPULATION_SIZE)
best_bee = min(bees, key=FUN)

for _ in range(GENERATIONS):
    bees = search_bees()
    bees = recruit_bees(bees, best_bee)
    local_search(bees)
    best_bee_in_iteration = min(bees, key=FUN)
    if FUN(best_bee_in_iteration) < FUN(best_bee):
        best_bee = list(best_bee_in_iteration)

print("Najlepszy osobnik: {}".format(best_bee))
print("Wynik f(x) = {}".format(FUN(best_bee)))