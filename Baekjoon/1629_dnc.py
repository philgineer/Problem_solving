def dnc(a, b):
    if b == 1:
        return a % c
    if b % 2 == 1:
        return dnc(a, b - 1) * a
    else:
        return (dnc(a, b // 2) % c) ** 2 % c

a, b, c = map(int, input().split())
print(dnc(a, b) % c)