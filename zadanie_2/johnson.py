"""
Algorytm Johnsona w wersji wykorzystującej algorytmy Dijkstry oraz Bellmana-Forda

Autor:  <@student.polsl.pl>
Data: 08-03-2023
"""


def min_distance(dist, visited):
    # Funkcja pomocnicza symulujaca kolejke priorytetowa w algorytmie Dijkstry
    min = float('inf')
    min_v = 0

    for v in range(len(dist)):
        if min > dist[v] and not visited[v]:
            min = dist[v]
            min_v = v

    return min_v


def dijkstra(graph, start_from):
    # Tablica odleglosci od zrodla dla wszystkich wierzcholkow
    dist = [float('inf')] * len(graph)
    dist[start_from] = 0

    # Tablica odwiedzonych wierzcholkow
    visited = [False] * len(graph)

    for i in range(len(graph)):
        # Znajdz najblizszy zrodla nieodwiedzony wierzcholek
        u = min_distance(dist, visited)

        # Oznacz go jako odwiedzony
        visited[u] = True

        # Dokonanie relaksacji zgodnie ze wzorem
        for v in range(len(graph)):
            if graph[u][v] is not None:
                if not visited[v] and dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]

    # Wypisz tablice najkrotszych odleglosci do wszystkich wierzcholkow
    for i in range(len(dist)):
        if dist[i] != float('inf') and start_from != i:
            print('Najkrotsza sciezka z #{} do #{} ma dlugosc: {}'.format(
                start_from, i, dist[i]))


def bellman_ford(graph):
    # Stworzenie listy krawedzi na potrzeby algorytmu Bellmana-Forda
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] is not None:
                edges.append([i, j, graph[i][j]])

    # Dodanie nowego sztucznego wezla pomocniczego o wagach 0
    for i in range(len(graph)):
        edges.append([len(graph), i, 0])

    # Tablica odleglosci od wierzcholka startowego (pomocniczego wezla)
    dist = [float('inf')] * (len(graph) + 1)
    dist[len(graph)] = 0

    # Dokonanie relaksacji zgodnie ze wzorem
    for i in range(len(graph)):
        for (u, v, w) in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Zwroc wynik z pominienieciem pomocniczego wezla zerowego
    return dist[0:len(graph)]


def johnson(graph):
    # Wykorzystanie algorytmu Bellmana-Forda do znalezienia minimalnych odleglosci od sztucznego wezla pomocniczego
    bellman_dist = bellman_ford(graph)

    # Przewagowanie grafu celem zlikwidowania ujemnych wag
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] is not None:
                graph[i][j] = graph[i][j] + bellman_dist[i] - bellman_dist[j]

    # Wykonanie algorytmu Dijkstry dla kazdego wierzcholka w grafie
    for i in range(len(graph)):
        dijkstra(graph, i)


if __name__ == "__main__":
    # Graf w postaci tablicy sasiedztwa z wagami krawedzi
    graph = [
        [None, -2, None, None, None, None],
        [None, None, -1, None, None, None],
        [4, None, None, 2, -3, None],
        [None, None, None, None, None, None],
        [None, None, None, None, None, None],
        [None, None, None, 1, -4, None],
    ]

    # Wykonanie algorytmu Johnsona
    johnson(graph)
