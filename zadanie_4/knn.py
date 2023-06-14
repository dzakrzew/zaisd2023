"""
Algorytm K-Najbliższych Sąsiadów KNN

Autor:  <@student.polsl.pl>
Data: 25-03-2023
"""

from math import sqrt

def dist(x1, x2):
    return sqrt(sum((p1 - p2)**2 for p1, p2 in zip(x1, x2)))

def knn(data, query, k):
    neighbor_distances_and_indices = []

    for index, (features, label) in enumerate(data):
        distance = dist(features, query)
        neighbor_distances_and_indices.append((distance, index))

    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)

    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]

    k_nearest_labels = [data[i][1] for distance, i in k_nearest_distances_and_indices]

    return max(set(k_nearest_labels), key=k_nearest_labels.count)


# https://www.freecodecamp.org/news/content/images/2023/01/knn-data-graph-2.png
data = [
    ((6, 15), 'Red'),
    ((4, 22), 'Red'),
    ((8, 20), 'Red'),
    ((12, 15), 'Red'),
    ((13, 25), 'Red'),
    ((12, 31), 'Red'),
    ((16, 28), 'Red'),
    ((16, 49), 'Blue'),
    ((25, 50), 'Blue'),
    ((25, 61), 'Blue'),
    ((29, 49), 'Blue'),
    ((29, 58), 'Blue'),
    ((30, 69), 'Blue')
]

print(knn(data, (23, 50), k=2))  # Wynik: Blue
print(knn(data, (5, 10), k=2))  # Wynik: Red
print(knn(data, (16, 36), k=2))  # Wynik: ??
