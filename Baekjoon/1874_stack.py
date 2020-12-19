n = int(input())

def stack_seq():
    seq = [int(input()) for _ in range(n)]
    n_list = [i + 1 for i in range(n)]
    stack = []
    res = []
    i = 0
    j = 0
    while i < n:
        if stack and (stack[-1] == seq[i]):
            stack.pop()
            i += 1
            res.append('-')
        else:
            if j >= n:
                return
            stack.append(n_list[j])
            j += 1
            res.append('+')
    return res

res = stack_seq()
if res:
    for sign in res:
        print(sign)
else:
    print("NO")