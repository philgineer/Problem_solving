n, r, c = map(int, input().split())

mat = [[-1] * (2 ** n) for _ in range(2 ** n)]
print(mat)

def divide(row, col, size, num):
    if mat[r][c] != -1:
        print(mat)
        return
    elif size == 2:
        for i in range(2):
            for j in range(2):
                mat[row + i][col + j] = num + 2 * i + j
    else:
        divide(row, col, size//2, num)
        divide(row, col + size//2, size//2, num + (size//2) ** 2)
        divide(row + size//2, col, size//2, num + (size//2) ** 2 * 2)
        divide(row + size//2, col + size//2, size//2, num + (size//2) ** 2 * 3)

divide(0,0,2 ** n,0)

for m in mat:
    print(m)

print(mat[r][c])