"""
Algorytm nietoperza (bat algorithm)

Autor:  <@student.polsl.pl>
Data: 11-04-2023
"""

import random
import math
from test_functions import sphere_fun

N = 3 # wymiar funkcji
GENERATIONS = 1000 # liczba generacji
POPULATION_SIZE = 50 # rozmiar populacji
FUN = sphere_fun # wybrana funkcja
FUN_RANGE = [-10, 10] # przedzial funkcji

ALPHA = 0.9
GAMMA = 0.9
LOUDNESS = 0.5
PULSE_RATE = 0.5
FREQ_MIN = 0
FREQ_MAX = 2

def init_bats():
    bats = [{'position': [random.uniform(FUN_RANGE[0], FUN_RANGE[1]) for _ in range(N)], 'frequency': 0, 'velocity': [0]*N, 'loudness': LOUDNESS, 'rate': PULSE_RATE} for _ in range(POPULATION_SIZE)]
    return bats

def update_bat(bat, best_bat):
    beta = random.random()
    bat['frequency'] = FREQ_MIN + (FREQ_MAX - FREQ_MIN) * beta

    for i in range(len(bat['position'])):
        bat['velocity'][i] += (bat['position'][i] - best_bat['position'][i]) * bat['frequency']
        bat['position'][i] += bat['velocity'][i]

        if bat['position'][i] < FUN_RANGE[0]: bat['position'][i] = FUN_RANGE[0]
        if bat['position'][i] > FUN_RANGE[1]: bat['position'][i] = FUN_RANGE[1]
    
    if random.random() > bat['rate']:
        for i in range(len(bat['position'])):
            bat['position'][i] = best_bat['position'][i] + random.uniform(-1, 1)

            if bat['position'][i] < FUN_RANGE[0]: bat['position'][i] = FUN_RANGE[0]
            if bat['position'][i] > FUN_RANGE[1]: bat['position'][i] = FUN_RANGE[1]
    
    if random.random() < bat['loudness'] and FUN(bat['position']) < FUN(best_bat['position']):
        bat['loudness'] *= ALPHA
        bat['rate'] = bat['rate'] if bat['rate'] < 0 else bat['rate'] * (1 - math.exp(-GAMMA))


bats = init_bats()
best_bat = min(bats, key=lambda bat: FUN(bat['position']))

for _ in range(GENERATIONS):
    for bat in bats:
        update_bat(bat, best_bat)

        if FUN(bat['position']) < FUN(best_bat['position']):
            best_bat = bat


print("Najlepszy osobnik: {}".format(best_bat['position']))
print("Wynik f(x) = {}".format(FUN(best_bat['position'])))