
"""
Algorytm wyznaczania drzewa spinającego (Prima)

Autor:  <@student.polsl.pl>
Data: 13-03-2023
"""

def prim(graph, start_v = 0):
    # Liczba wierzcholkow
    n = len(graph)

    # Inicjowanie tablicy odwiedzonych wierzcholkow
    visited = [False] * n

    # Oznaczenie startowego wierzcholka jako odwiedzony
    visited[start_v] = True

    # Zbior krawedzi
    edges = []

    for edge in range(n):
        min_edge = [None, None, float('inf')]
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j]:
                        if min_edge[2] > graph[i][j]:
                            min_edge = [i, j, graph[i][j]]
        if min_edge[2] != float('inf'):
            edges.append(min_edge)
            visited[min_edge[1]] = True

    return edges

def print_path(edges):
    for e in edges:
        print(f"{e[0]} -> {e[1]} (Waga: {e[2]})")

if __name__ == "__main__":
    # https://eduinf.waw.pl/inf/alg/001_search/images/0141_01.gif
    graph = [
        #0 #1 #2 #3 #4 #5 #6 #7
        [0, 5, 0, 9, 0, 0, 3, 0], #0
        [5, 0, 9, 0, 8, 6, 0, 7], #1
        [0, 9, 0, 9, 4, 0, 5, 3], #2
        [9, 0, 9, 0, 0, 0, 8, 0], #3
        [0, 8, 4, 0, 0, 2, 1, 0], #4
        [0, 6, 0, 0, 2, 0, 6, 0], #5
        [3, 0, 5, 8, 1, 6, 0, 9], #6
        [0, 7, 3, 0, 0, 0, 9, 0], #7
    ]

    path = prim(graph)

    # Wypisanie wyniku - minimalnego drzewa wraz z wagami
    print_path(path)