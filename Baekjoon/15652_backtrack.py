def backtrack(s, n, m):
    if len(s) == m:
        print(' '.join(s))
        return
    if s:
        now = int(s[-1])
    else:
        now = 1
    for i in range(now, n + 1):
        backtrack(s + str(i), n, m)
        
n, m = map(int, input().split())
backtrack('', n, m)