import math

x = [1, 2, 3]
y = [0, 1, 1]  # Logistic regression expects 0 or 1 targets

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def logistic_regression(x, y):
    epochs = 5
    n = len(x)
    w = 0.5
    b = 0.5
    learning_rate = 0.1

    for epoch in range(epochs):
       
        y_hat = []
        for i in range(n):
            z = w * x[i] + b
            y_hat.append(sigmoid(z))

        
        loss = 0
        for i in range(n):
            # Avoid log(0)
            y_hat_clipped = max(min(y_hat[i], 1-1e-15), 1e-15)
            loss += - (y[i] * math.log(y_hat_clipped) + (1 - y[i]) * math.log(1 - y_hat_clipped))
        loss = loss / n

        
        dw = 0
        db = 0
        for i in range(n):
            dw += x[i] * (y_hat[i] - y[i])
            db += (y_hat[i] - y[i])
        dw = dw / n
        db = db / n

        
        w = w - learning_rate * dw
        b = b - learning_rate * db

        print(f"Epoch: {epoch + 1}, Loss: {loss:.4f}, w: {w:.4f}, b: {b:.4f}")
        print(f"  y_hat: {[round(v,2) for v in y_hat]}")

logistic_regression(x, y)
