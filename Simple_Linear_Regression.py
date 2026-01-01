x=[1,2,3]
y=[2,4,6]


def linear_regression(x,y):
    epochs = 5
    n = len(x)
    w = 0.5
    b = 0.5
    learning_rate = 0.1
    
    for epoch in range(epochs):

        y_hat = []

        for i in range(n):
            y_hat.append(w * x[i] + b)

        loss = 0
        for i in range(n):
            loss += (y[i] - y_hat[i])**2
        loss = loss/n
        
        dw = 0
        db = 0
        for  i in range(n):
            dw += x[i] * (y[i] -  y_hat[i])
            db += (y[i] - y_hat[i])

        dw = -2 * dw/n
        db = -2 * db/n

        w = w - learning_rate * dw
        b = b - learning_rate * db

        print(f"Epoch: {epoch + 1}, Loss: {loss:.4f} , w: {w:.4f} , b: {b:.4f}")
        print(f"  y_hat: {[round(v,2) for v in y_hat]}")

linear_regression(x,y)


    


    