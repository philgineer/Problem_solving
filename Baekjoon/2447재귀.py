def make_null(col, row, size):
    for i in range(size):
        for j in range(size):
                res[col + i][row + j] = ' '
    
def make_star(col, row, size):
    if (size == 3):
        for i in range(3):
            for j in range(3):
                if i == j and j == 1:
                    res[col + i][row + j] = ' '
                else:
                    res[col + i][row + j] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i == j and j == 1:
                make_null(col + (size//3)*i, row + (size//3)*j, (size//3))
            else:
                make_star(col + (size//3)*i, row + (size//3)*j, (size//3))
    return

n = int(input())
res = list()
for i in range(n):
    res.append(['_' for j in range(n)])

make_star(0, 0, n)
for i in range(n):
    for j in range(n):
        print(res[i][j], end='')
    print()