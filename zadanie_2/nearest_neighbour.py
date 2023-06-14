"""
Algorytm najbliższego sąsiada

Autor:  <@student.polsl.pl>
Data: 07-03-2023
"""

from time import sleep

def nearest_neighbour(graph, current, visited = []):
    # Jezeli odwiedzono wszystkie wierzcholki, zwroc wynik
    if len(visited) == len(graph):
        return visited

    # Ustaw aktualny wierzcholek jako odwiedzony
    visited.append(current)

    # Znajdz nieodwiedzony wierzcholek polaczony z obecnym krawedzia o najmniejszej wadze
    min_index = None
    min_weight = float('inf')

    for i in range(len(graph)):
        if i not in visited and graph[current][i] < min_weight:
            min_weight = graph[current][i]
            min_index = i

    return nearest_neighbour(graph, min_index, visited)

def print_path(visited):
    print(' -> '.join([str(i) for i in visited]) + ' --> ' + str(visited[0]))

if __name__ == "__main__":
    # Graf w postaci tablicy sasiedztwa z wagami krawedzi
    graph = [
        [0, 4, 5, 6, 1],
        [4, 0, 6, 4, 7],
        [5, 6, 0, 7, 2],
        [6, 4, 7, 0, 3],
        [1, 7, 2, 3, 0],
    ]

    # Wyznaczanie minimalnego cyklu
    path = nearest_neighbour(graph, 0)

    # Wypisanie cyklu za pomoca funkcji pomocniczej
    print_path(path)
