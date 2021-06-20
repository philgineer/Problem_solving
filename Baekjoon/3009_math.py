import sys

X = []
Y = []
res = [0, 0]
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)
for x in X:
    if X.count(x) == 1:
        res[0] = x
for y in Y:
    if Y.count(y) == 1:
        res[1] = y
print(res[0], res[1])