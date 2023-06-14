"""
Algorytm KNN dla centroidów

Autor:  <@student.polsl.pl>
Data: 25-03-2023
"""

from math import sqrt

def dist(x1, x2):
    return sqrt(sum((p1 - p2)**2 for p1, p2 in zip(x1, x2)))

def calculate_centroids(data):
    class_points = {}
    class_counts = {}

    for features, label in data:
        if label not in class_points:
            class_points[label] = [0] * len(features)
            class_counts[label] = 0
        for i, value in enumerate(features):
            class_points[label][i] += value
        class_counts[label] += 1

    centroids = {}

    for label, points in class_points.items():
        centroids[label] = [value / class_counts[label] for value in points]
    
    return centroids

def knn_centroids(data, query):
    centroids = calculate_centroids(data)
    distances = []
    
    for label, centroid in centroids.items():
        distance = dist(centroid, query)
        distances.append((distance, label))

    _, closest_label = min(distances)
    return closest_label


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

print(knn_centroids(data, (23, 50)))  # Wynik: Blue
print(knn_centroids(data, (5, 10)))  # Wynik: Red
print(knn_centroids(data, (16, 36)))  # Wynik: ??
