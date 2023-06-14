"""
Algorytm roju cząstek (particle swarm algorithm)

Autor:  <@student.polsl.pl>
Data: 07-05-2023
"""

import random
from test_functions import sphere_fun

N = 3 # wymiar funkcji
GENERATIONS = 1000 # liczba generacji
PARTICLES_NUMBER = 30 # liczba cząstek
FUN = sphere_fun # wybrana funkcja
C1 = 1 # współczynnik korekcji
C2 = 1 # współczynnik korekcji
W = 0.5 # parametr w
FUN_RANGE = [-10, 10] # przedzial funkcji

def generate_particles():
    return [[[random.uniform(FUN_RANGE[0], FUN_RANGE[1]) for _ in range(N)],  # pozycja
             [random.uniform(-1, 1) for _ in range(N)],                       # velocity
             float('inf')]                                                    # najlepsza pozycja
            for _ in range(PARTICLES_NUMBER)]

def update_velocity(particle, global_best_position):
    for i in range(len(particle[1])):
        r1 = random.random()
        r2 = random.random()
        cognitive_velocity = C1 * r1 * (particle[2] - particle[0][i])
        social_velocity = C2 * r2 * (global_best_position[i] - particle[0][i])
        particle[1][i] = W * particle[1][i] + cognitive_velocity + social_velocity

def update_position(particle):
    for i in range(len(particle[0])):
        particle[0][i] = particle[0][i] + particle[1][i]
        if particle[0][i] > FUN_RANGE[1]:
            particle[0][i] = FUN_RANGE[1]
        if particle[0][i] < FUN_RANGE[0]:
            particle[0][i] = FUN_RANGE[0]

particles = generate_particles()
global_best_position = particles[0][0]
global_best_value = float('inf')

for _ in range(GENERATIONS):
    for particle in particles:
        fitness = FUN(particle[0])
        if fitness < particle[2]:
            particle[2] = fitness
        if fitness < global_best_value:
            global_best_position = particle[0]
            global_best_value = fitness

        update_velocity(particle, global_best_position)
        update_position(particle)

print("Najlepszy: {}".format(global_best_position))
print("Wynik f(x) = {}".format(global_best_value))