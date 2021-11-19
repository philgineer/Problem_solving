def cal(s):
    res = 0
    for c in s:
        if c in '0123456789':
           res += int(c)
    return res

n = int(input())
guitars = []
for _ in range(n):
    s = input()
    guitars.append((s, cal(s), len(s)))
    
for i in range(3):
    guitars.sort(key=lambda x: x[i])
    
for g in guitars:
    print(g[0])