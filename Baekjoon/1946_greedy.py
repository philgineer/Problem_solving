import sys

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    ranks = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ranks.sort()
    #print(ranks)
    res = 1
    best = ranks[0][1]
    for i in range(1, n):
        if best > ranks[i][1]:
            res += 1
            best = ranks[i][1]
            #print('ranks[{}]:'.format(i),ranks[i])
    out.append(res)
for o in out:
    print(o)