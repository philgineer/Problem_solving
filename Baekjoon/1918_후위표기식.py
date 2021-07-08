l = list(input()) + ['<EOS>']
bracket_dict = {1: ')', -1: '('}

def skip_bracket(l, i, j, direction):
    bracket = 1
    while bracket:
        if l[j] == '(':
            bracket += direction
        elif l[j] == ')':
            bracket -= direction
        j += direction
    l.insert(j + (direction == -1), bracket_dict[direction])

for step in ['*/', '+-']:
    i = 0
    while l[i] != '<EOS>':
        next_idx = i + 1
        if l[i] in step:
            if l[i-1] == ')':
                j = i-2
                skip_bracket(l, i, j, -1)
                next_idx += 1
                if l[i+2] == '(':
                    j = i+3
                    skip_bracket(l, i, j, 1)
                else:
                    l.insert(i+3, ')')
            else:
                l.insert(i-1, '(')
                next_idx += 1
                if l[i+2] == '(':
                    j = i+3
                    skip_bracket(l, i, j, 1)
                else:
                    l.insert(i+3, ')')
        i = next_idx

    print(' '.join(l))


res = ['0'] * len(l)
i = 0
add = 0
while l[i] != '<EOS>':
    if l[i] in '+-*/':
        bracket = 0
        j = i+1
        while True:
            if l[j] == '(':
                bracket += 1
            elif l[j] == ')':
                bracket -= 1
            j += 1
            if bracket == 0 or l[j] == '<EOS>':
                break
        res.insert(j+add, l[i])
        add += 1
    elif l[i] not in '()':
        res.insert(i+add, l[i])
        add += 1
    i += 1

print(''.join(x for x in res if x != '0'))