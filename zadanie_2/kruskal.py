"""
Algorytm Kruskala wyznaczania drzewa spinającego

Autor:  <@student.polsl.pl>
Data: 09-03-2023
"""

def find_root(roots, i):
    # Funkcja znajdujaca wierzcholek bedacy korzeniem drzewa
    if roots[i] != i:
        roots[i] = find_root(roots, roots[i])
    return roots[i]

def connect_trees(roots, ranks, u, v):
    # Funkcja pomocnicza do laczenia dwoch drzew
    # Drzewo o najmniejszej randze korzenia podpinane jest pod drzewo wyzszej rangi
    if ranks[u] < ranks[v]:
        roots[u] = v
    elif ranks[v] < ranks[u]:
        roots[v] = u
    else:
        roots[u] = v
        ranks[v] += 1

def kraskal(edges):
    # Pomocnicze utworzenie listy wierzcholkow z listy krawedzi
    vertices_count = max(edges, key=lambda e: e[1])[1] + 1
    vertices = list(range(vertices_count))

    # Wierzcholki-korzenie drzew (poczatkowo kazdy wierzcholek jest korzeniem wlasnego drzewa)
    roots = list(range(vertices_count))

    # Rangi korzeni w drzewie
    ranks = [0] * len(vertices)

    # Sortowanie krawedzi wg wagi (od najmniejszego do najwiekszego)
    edges_sorted = sorted(edges, key=lambda e: e[2])

    # Las wynikowy [(source, dest, weight), ...]
    forest = []

    # Suma wag
    weight_sum = 0

    while len(edges_sorted) > 0:
        # Wybierz i usun krawedz o minimalnej wadze
        u, v, w = edges_sorted.pop(0)

        # Zidentyfikuj korzenie wybranych krawedzi
        u_root = find_root(roots, u)
        v_root = find_root(roots, v)

        # Sprawdzanie czy krawedz laczy dwa rozne drzewa
        if u_root != v_root:
            # ...jezeli laczy, dodaj ja do lasu i polacz dwa drzewa w jedno
            forest.append([u, v, w])
            connect_trees(roots, ranks, u_root, v_root)
            weight_sum += w

    # Wyswietlanie wyniku
    print('Minimalne drzewa rozpinajace (dlugosc {}):'.format(weight_sum))

    for t in forest:
        print('{} --({})--> {}'.format(t[0], t[1], t[2]))

if __name__ == "__main__":
    # Graf w postaci listy krawedzi z wagami
    # https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Kruskal_Algorithm_6.svg/200px-Kruskal_Algorithm_6.svg.png
    edges = [
        [0, 1, 7],
        [0, 3, 5],
        [1, 3, 9],
        [1, 2, 8],
        [2, 4, 5],
        [1, 4, 7],
        [3, 4, 15],
        [3, 5, 6],
        [5, 6, 11],
        [4, 5, 8],
        [4, 6, 9]
    ]

    kraskal(edges)