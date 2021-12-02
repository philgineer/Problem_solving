def rev_string(s):
    new = ''
    for i in range(len(s)-1, -1, -1):
        new += s[i]
    return new

def solve(s, t):
    global done
    if done:
        return 0
    if len(s) == len(t):
        if s == t:
            done = True
            return 1
        else:
            return 0
    case1 = solve(s + 'A', t)
    case2 = solve(rev_string(s) + 'B', t)
    return case1 + case2

s = input()
t = input()
done = False
print(solve(s, t))