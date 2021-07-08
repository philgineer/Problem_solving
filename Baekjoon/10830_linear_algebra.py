def mat_mul(A, B):
    R = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                R[i][j] += A[i][k] * B[k][j]
            R[i][j] %= 1000
    return R

n, b = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(n)]
b = bin(b)[2:]
res = [[1 if i==j else 0 for i in range(n)] for j in range(n)]
temp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        temp[i][j] = M[i][j]

for i in range(len(b)):
    if b[-1 - i] == '1':
        res = mat_mul(temp, res)
    temp = mat_mul(temp, temp)

for r in res:
    print(' '.join(str(x) for x in r))