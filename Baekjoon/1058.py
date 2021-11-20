n = int(input())
graph = []
for _ in range(n):
    l = []
    s = input()
    for i, c in enumerate(s):
        if c == 'Y':
            l.append(i)
    graph.append(l)
    
res = 0
for i in range(n):
    friend = graph[i]
    friend2 = set(friend)
    for f in friend:
        friend2 = friend2.union(graph[f])
    temp = len(friend2)
    if temp > res:
        res = temp
print(max(res - 1, 0))