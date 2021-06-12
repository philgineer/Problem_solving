import sys
input = sys.stdin.readline

def distance(br, bc, r, c, mat):
    


n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * n for _ in range(n)]

print('MAT')
for m in mat:
    print(m)

b_size = 2
cnt = 0
br, bc = 0, 0
fish = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 9:
            br, bc = i, j
        elif mat[i][j] != 0:
            fish.append((i,j,mat[i][j])) # (r, c, size)
            if mat[i][j] > b_size:
                temp[i][j] = 1

print('fish:',fish)
print('baby: ({},{})'.format(br, bc))

print('TEMP')
for t in temp:
    print(t)