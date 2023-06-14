"""
Algorytm kukułki (cuckoo search)

Autor:  <@student.polsl.pl>
Data: 20-04-2023
"""

import random
from test_functions import sphere_fun

N = 3 # wymiar funkcji
GENERATIONS = 1000 # liczba generacji
NESTS_NUMBER = 20 # rozmiar populacji (gniazd)
PA = 0.25 # parametr p_a (prawdopodobieństwo pozostawienia jaja)
STEP_SIZE = 0.1
FUN_RANGE = [-10, 10] # przedzial funkcji
FUN = sphere_fun # wybrana funkcja

def get_random_cuckoo(nests, best_nest):
    n = random.randint(0, len(nests) - 1)

    while nests[n] == best_nest:
        n = random.randint(0, len(nests) - 1)
    
    return nests[n]

def move_cuckoo(nest, best_nest):
    cuckoo = [n + STEP_SIZE * (n - bn) for n, bn in zip(nest, best_nest)]
    return cuckoo

def replace_nest(nests, new_nest):
    n = random.randint(0, len(nests) - 1)

    if FUN(nests[n]) > FUN(new_nest):
        nests[n] = new_nest
    
    return nests

def abandon_nest(nests):
    for i in range(len(nests)):
        if random.random() < PA:
            nests[i] = [random.uniform(FUN_RANGE[0], FUN_RANGE[1]) for _ in range(N)]
    
    return nests

nests = [[random.uniform(FUN_RANGE[0], FUN_RANGE[1]) for i in range(N)] for _ in range(NESTS_NUMBER)]

fitness = [FUN(nest) for nest in nests]
best_nest = nests[fitness.index(min(fitness))]

for _ in range(GENERATIONS):
    nest = get_random_cuckoo(nests, best_nest)
    new_nest = move_cuckoo(nest, best_nest)
    nests = replace_nest(nests, new_nest)
    nests = abandon_nest(nests)
    fitness = [FUN(nest) for nest in nests]
    current_best_nest = nests[fitness.index(min(fitness))]

    if FUN(current_best_nest) < FUN(best_nest):
        best_nest = current_best_nest


print("Najlepszy osobnik: {}".format(best_nest))
print("Wynik f(x) = {}".format(FUN(best_nest)))