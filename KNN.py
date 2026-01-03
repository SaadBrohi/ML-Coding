X = [
    [1, 2],
    [2, 3],
    [3, 1],
    [6, 5],
    [7, 7],
    [8, 6]
]
y = ['A', 'A', 'A', 'B', 'B', 'B']

def euclidean_distance(a, b):
    dist = 0
    for i in range(len(a)):
        dist += (a[i] - b[i]) ** 2
    return dist ** 0.5

def knn(X_train, y_train, X_test, k=3):
    predictions = []
    for x in X_test:
        distances = []
        for i in range(len(X_train)):
            dist = euclidean_distance(x, X_train[i])
            distances.append((dist, y_train[i]))
        
        for i in range(len(distances)):
            for j in range(i+1, len(distances)):
                if distances[i][0] > distances[j][0]:
                    distances[i], distances[j] = distances[j], distances[i]
        
        votes = {}
        for i in range(k):
            label = distances[i][1]
            if label in votes:
                votes[label] += 1
            else:
                votes[label] = 1
        
        max_vote = -1
        pred = None
        for label in votes:
            if votes[label] > max_vote:
                max_vote = votes[label]
                pred = label
        
        predictions.append(pred)
    return predictions

X_test = [
    [2, 2],
    [7, 5]
]

predictions = knn(X, y, X_test, k=3)
print(predictions)
