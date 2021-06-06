import copy

def solution(n, k, cmd):
    original = [i for i in range(n)]
    table = copy.deepcopy(original)
    cur_idx = k
    temp = []
    res = ''

    for c in cmd:
        if c =='Z':
            idx, val = temp.pop()
            table.insert(idx, val)
            if idx <= cur_idx:
                cur_idx += 1    
        elif c[0] == 'D':
            cur_idx += int(c[2:])
        elif c[0] == 'U':
            cur_idx -= int(c[2:])
        else:
            current = table[cur_idx]
            temp.append((cur_idx, current))
            if current == table[-1]:
                table.pop(-1)
                cur_idx -= 1
            else:
                table.pop(cur_idx)

    i, j = 0, 0
    len_o, len_t = len(original), len(table)
    while j < len_o:
        if i < len_t and table[i] == original[j]:
            res += 'O'
            i += 1
        else:
            res += 'X'
        j += 1

    return res