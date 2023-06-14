"""
Algorytm kolorowania wierzchołków LF

Autor:  <@student.polsl.pl>
Data: 10-03-2023
"""

def lf(g):
    # Oblicz stopnie wierzchołków grafu
    d = [sum(row) for row in g]
    
    # Sortuj wierzchołki wg stopnia rosnąco
    nodes = sorted(range(len(g)), key=lambda x: d[x], reverse=True)

    # Zainicjuj mapę kolorów
    color_map = {}

    for i in range(len(nodes)):
        v = nodes[i]
        available_colors = [True] * len(g)

        for j in range(len(g[v])):
            if g[v][j] and j in color_map:
                available_colors[color_map[j]] = False

        for c in range(len(available_colors)):
            if available_colors[c]:
                color_map[v] = c
                break

    return color_map

def print_colors(color_map):
    for v, color in color_map.items():
        print('Wierzchołek {} ma kolor {}'.format(v, color))

if __name__ == "__main__":
    # https://eduinf.waw.pl/inf/alg/001_search/images/0142_11.gif
    g = [
        #0 #1 #2 #3 #4 #5 #6 #7 #8
        [0, 1, 0, 1, 1, 0, 0, 0, 0], #0
        [1, 0, 1, 1, 0, 1, 0, 0, 0], #1
        [0, 1, 0, 1, 1, 1, 0, 1, 0], #2
        [1, 1, 1, 0, 1, 0, 1, 1, 0], #3
        [1, 0, 1, 1, 0, 1, 1, 0, 1], #4
        [0, 1, 1, 0, 1, 0, 1, 1, 1], #5
        [0, 1, 0, 1, 1, 1, 0, 1, 0], #6
        [0, 0, 1, 1, 0, 1, 1, 0, 1], #7
        [0, 0, 0, 0, 1, 1, 0, 1, 0], #8
    ]

    color_map = lf(g)
    print_colors(color_map)