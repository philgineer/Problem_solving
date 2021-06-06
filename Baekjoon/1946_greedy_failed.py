### 시간 초과 ###

import sys

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    ranks = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ranks.sort(reverse=True)
    #print(ranks)
    res = 1
    for i in range(n-1):
        flag = 1
        for j in range(i+1, n):
            if ranks[i][1] > ranks[j][1]:
                #print('ranks[{}] failed because of ranks[{}]'.format(i, j))
                flag = 0
                break
        if flag:
            #print('ranks[{}] passed'.format(i))
            res += 1
    out.append(res)
for o in out:
    print(o)