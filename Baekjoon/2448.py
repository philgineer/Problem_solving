def tree(row, col, size):
    if size == 3:
        for i in range(5):
            graph[row][col - i] = '*'
            if i % 2 == 1:
                graph[row - 1][col - i] = '*'
            if i == 2:
                graph[row - 2][col - i] = '*'
    elif size == 6:
        tree(row, col, 3)
        tree(row, col-6, 3)
        tree(row-3, col-3, 3)
    else:
        tree(row, col, size // 2)
        tree(row, col - size, size // 2)
        tree(row - size // 2, col - size * 1 // 2, size // 2)

n = int(input())
width = (n//3)*5 + (n//3) - 1
graph = [[' ']* width for _ in range(n)]
tree(n-1, width-1, n)

for g in graph:
    print(''.join(g))