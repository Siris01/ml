from tabulate import tabulate

w0 = float(input("Enter value of w0: "))
w1 = float(input("Enter value of w1: "))
w2 = float(input("Enter value of w2: "))

bias = float(input("Enter value of bias: "))
epochs = int(input("Enter number of epochs (0 to proceed until convergence): "))
learning_rate = float(input("Enter learning rate: "))
theta = float(input("Enter theta: "))
print()

curr_epochs = 0

OR_NETWROK = [(1, 1, 1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1)]

while True if epochs == 0 else (curr_epochs < epochs):
    curr_epochs = curr_epochs + 1
    print("epoch #", curr_epochs)

    converged = True
    table = []

    for x1, x2, t in OR_NETWROK:
        y = bias*w0 + x1*w1 + x2*w2
        y = 1 if y >= theta else -1
        if y != t: converged = False

        w0 = w0 + learning_rate*(t - y)*bias
        w1 = w1 + learning_rate*(t - y)*x1
        w2 = w2 + learning_rate*(t - y)*x2

        table.append([x1, x2, t, y, w0, w1, w2])

    print(tabulate(table, headers=["x1", "x2", "t", "y", "w0", "w1", "w2"], tablefmt="orgtbl"))

    if converged:
        print("Converged at epoch #", curr_epochs)
        break
    
    print()