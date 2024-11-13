with open("input.txt", "r") as f:
    X = f.read().splitlines()

x1,x2 = X[:2]

x1 = x1.split("@").split(",")
x2 = x2.split("@").split(",")