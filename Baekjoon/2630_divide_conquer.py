n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
white, blue = 0, 0

def split_square(mat, size):
    global white, blue
    splited = [[], [], [], []]
    for i in range(size//2):
        splited[0].append(mat[i][:size//2]) # left_up
        splited[1].append(mat[size//2 + i][:size//2]) # left_down
        splited[2].append(mat[i][size//2:]) # right_up
        splited[3].append(mat[size//2 + i][size//2:]) # right_down
    for square in splited:
        s = sum([sum(row) for row in square])
        if s == 0:
            white += 1
        elif s == pow(size//2, 2):
            blue += 1
        else:
            split_square(square, size//2)

split_square(mat, n)
print(white)
print(blue)