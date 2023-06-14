"""
Algorytm świetlika (firefly algorithm)

Autor:  <@student.polsl.pl>
Data: 26-04-2023
"""

import random
import math
from test_functions import sphere_fun

N = 3 # wymiar funkcji
GENERATIONS = 1000 # liczba generacji
POPULATION_SIZE = 20 # rozmiar populacji
FUN = sphere_fun # wybrana funkcja
FUN_RANGE = [-10, 10] # przedzial funkcji

ALPHA = 0.5
BETA0 = 1
GAMMA = 1

def init_fireflies():
    return [{'position': [random.uniform(FUN_RANGE[0], FUN_RANGE[1]) for i in range(N)]} for _ in range(POPULATION_SIZE)]

def attractiveness(r):
    return BETA0 * math.exp(-GAMMA * r**2)


def move_firefly(i, j, fireflies):
    r = math.sqrt(sum([(xi - xj)**2 for xi, xj in zip(fireflies[i]['position'], fireflies[j]['position'])]))

    for k in range(N):
        beta = attractiveness(r)
        fireflies[i]['position'][k] += beta * (fireflies[j]['position'][k] - fireflies[i]['position'][k]) + ALPHA * (random.uniform(0, 1) - 0.5)

        if fireflies[i]['position'][k] < FUN_RANGE[0]: fireflies[i]['position'][k] = FUN_RANGE[0]
        if fireflies[i]['position'][k] > FUN_RANGE[1]: fireflies[i]['position'][k] = FUN_RANGE[1]

fireflies = init_fireflies()

for _ in range(GENERATIONS):
    fireflies.sort(key=lambda x: FUN(x['position']))
    
    for i in range(POPULATION_SIZE):
        for j in range(POPULATION_SIZE):
            if FUN(fireflies[i]['position']) > FUN(fireflies[j]['position']):
                move_firefly(i, j, fireflies)

print("Najlepszy osobnik: {}".format(fireflies[0]['position']))
print("Wynik f(x) = {}".format(FUN(fireflies[0]['position'])))