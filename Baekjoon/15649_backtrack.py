def backtrack(s, n, m):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for next in range(1, n+1):
        if next not in s:
            s.append(next)
            backtrack(s, n, m)
            s.pop()
            
n, m = map(int, input().split())
backtrack([], n, m)