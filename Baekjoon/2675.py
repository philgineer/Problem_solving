t = int(input())
for _ in range(t):
    res = ''
    n, s = input().split()
    for c in s:
        res += c * int(n)
    print(res)