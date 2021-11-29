def backtrack(s, n, m):
    if len(s) == m:
        print(' '.join(s))
        return
    for i in range(1, n + 1):
        backtrack(s + str(i), n, m)
        
n, m = map(int, input().split())
backtrack('', n, m)