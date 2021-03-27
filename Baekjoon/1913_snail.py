n = int(input())
search_num = int(input())

map = [[0 for _ in range(n)] for _ in range(n)]
flag = ['down', 'right', 'up', 'left']
flag_idx = 0
i, j = 0, 0

def change_flag():
    global i, j, map, flag_idx
    if i < 0 or i >= n or j < 0 or j >= n or map[j][i] != 0:
        flag_idx += 1
        flag_idx = flag_idx % 4
        return True
    return False

for num in range(n ** 2, 0, -1):
    if num == search_num:
        s_j, s_i = j + 1, i + 1
    map[j][i] = str(num)

    if flag[flag_idx] == 'down':
        j += 1
        if change_flag():
            j -= 1
    if flag[flag_idx] == 'right':
        i += 1
        if change_flag():
            i -= 1
    if flag[flag_idx] == 'up':
        j -= 1
        if change_flag():
            j += 1
    if flag[flag_idx] == 'left':
        i -= 1
        if change_flag():
            i += 1
            j += 1

for i in range(n):
    print(' '.join(map[i]))
print(s_j, s_i)
