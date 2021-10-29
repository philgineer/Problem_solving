def backtrack(num, s, n, m):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for next in range(num, n+1):
        if next not in s:
            s.append(next)
            backtrack(next+1, s, n, m)
            s.pop()

n, m = map(int, input().split())
backtrack(1, [], n, m)