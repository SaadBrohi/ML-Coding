import random
import math

X = [
    [1, 2],
    [1, 4],
    [1, 0],
    [10, 2],
    [10, 4],
    [10, 0]
]

def euclidean_distance(a, b):
    dist = 0
    for i in range(len(a)):
        dist += (a[i] - b[i]) ** 2
    return dist ** 0.5

def kmeans(X, k=2, epochs=5):
    centroids = random.sample(X, k)

    for epoch in range(epochs):
        clusters = [[] for _ in range(k)]

        for x in X:
            min_dist = None
            cluster_idx = 0
            for i in range(k):
                dist = euclidean_distance(x, centroids[i])
                if min_dist is None or dist < min_dist:
                    min_dist = dist
                    cluster_idx = i
            clusters[cluster_idx].append(x)

        new_centroids = []
        for cluster in clusters:
            if cluster:
                centroid = []
                for i in range(len(cluster[0])):
                    s = 0
                    for point in cluster:
                        s += point[i]
                    centroid.append(s / len(cluster))
                new_centroids.append(centroid)
            else:
                new_centroids.append(random.choice(X))

        centroids = new_centroids

        print(f"Epoch {epoch+1}")
        for i in range(k):
            print(f"  Cluster {i+1}: {clusters[i]}")
        print(f"  Centroids: {[[round(c[0],2), round(c[1],2)] for c in centroids]}")
        print("-"*40)

kmeans(X, k=2, epochs=5)
