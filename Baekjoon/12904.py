def rev_string(s):
    new = ''
    for i in range(len(s)-1, -1, -1):
        new += s[i]
    return new

s = input()
t = input()
while len(t) != len(s):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = rev_string(t[:-1])
        
print(int(s == t))