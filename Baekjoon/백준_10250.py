def room_nbr(h, w, n):
    if n % h == 0:
        return h * 100 + (n // h)
    else:
        return (n % h) * 100 + (n // h) + 1

t = int(input())
res = []
for i in range(t):
    h, w, n = map(int, input().split())
    res.append(room_nbr(h, w, n))
for i in range(t):
    print(res[i])