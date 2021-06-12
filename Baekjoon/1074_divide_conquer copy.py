import sys

def divide(row, col, size, num):
    if 0 <= r - row < 2 and 0 <= c - col < 2:
        print(num + 2 * (r - row) + (c - col))
    elif row <= r < row + size//2:
        if col <= c < col + size//2:
            divide(row, col, size//2, num)
        else:
            divide(row, col + size//2, size//2, num + (size//2) ** 2)
    else:
        if col <= c < col + size//2:
            divide(row + size//2, col, size//2, num + (size//2) ** 2 * 2)
        else:
            divide(row + size//2, col + size//2, size//2, num + (size//2) ** 2 * 3)

n, r, c = map(int, sys.stdin.readline().split())
divide(0, 0, 2 ** n, 0)