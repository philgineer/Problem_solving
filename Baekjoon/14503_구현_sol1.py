import sys
input = sys.stdin.readline

dir_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move(row, col, d_cur):
    
    power_on = True
    print('\nBlock: ({},{}) , Direction: {}'.format(row, col, d_cur))
    d_start = d_cur
    print('Direction started from:',d_start)
    d_cur  = (d_cur + 3) % 4
    print('Direction changed:', d_cur)

    #1
    if clean[row][col] == 0:
        clean[row][col] = 1
        print('\ncleaned current block.')
    
    print('\nMAT')
    for ma in mat:
        print(ma)
    print('\nCLEAN')
    for cl in clean:
        print(cl)

    #2
    while power_on:
        r0, c0 = dir_list[d_cur]
        safe_idx = row + r0 >= 0 and row + r0 < n and col + c0 >= 0 and col + c0 < m
        safe_back = row - r0 >= 0 and row - r0 < n and col - c0 >= 0 and col - c0 < m

        if safe_idx and mat[row + r0][col + c0] == 0 and clean[row + r0][col + c0] == 0:
            print('\nleft side is available. turn left and go clean.')
            row += r0
            col += c0
            move(row, col, d_cur)
            break
        elif d_cur != d_start:
            print('\nleft side is unavailable. turn left twice.')
            d_cur = (d_cur + 3) % 4
        elif safe_back and mat[row - r0][col - c0] == 0:
            print("\nthere's no available side. go backstep.")
            move(row - r0, col - c0, d_cur)
            break
        else:
            print("\nthere's no available side and backside is wall.")
            power_on = False


n, m = map(int, input().split())
r, c, d = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
clean = [[0] * m for _ in range(n)]

print('\nMAT')
for ma in mat:
    print(ma)

print('\nCLEAN')
for cl in clean:
    print(cl)

move(r, c, d)

print('\nCLEAN')
for cl in clean:
    print(cl)

res = 0
for rc in clean:
    res += sum(rc)
print(res)