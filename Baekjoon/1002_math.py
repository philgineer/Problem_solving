import math

t = int(input())
res = []
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if dist == 0:
        if r1 == r2:
            res.append(-1)
        else:
            res.append(0)
    elif dist == r1 + r2 or dist == abs(r1 - r2):
        res.append(1)
    elif dist < r1 + r2 and abs(r1 - r2) < dist:
        res.append(2)
    else:
        res.append(0)
for r in res:
    print(r)