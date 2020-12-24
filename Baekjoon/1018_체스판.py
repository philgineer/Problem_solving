n, m = map(int, input().split())
X = [input() for _ in range(n)]

W = ('W B W B W B W B B W B W B W B W W B W B W B W B B W B W B W B W W B W B W B W B B W B W B W B W W B W B W B W B B W B W B W B W').split()
B = ('B W B W B W B W W B W B W B W B B W B W B W B W W B W B W B W B B W B W B W B W W B W B W B W B B W B W B W B W W B W B W B W B').split()

chesses = []
for i in range(n-7):
    for j in range(m-7):
        chess = []
        for a in range(8):
            for b in range(8):
                chess.append(X[i+a][j+b])
        chesses.append(chess)

diff_W = []
for i in range(len(chesses)):
    temp = []
    for j in range(64):
        temp.append(chesses[i][j] == W[j])
    diff_W.append(temp.count(0))
    
diff_B = []
for i in range(len(chesses)):
    temp = []
    for j in range(64):
        temp.append(chesses[i][j] == B[j])
    diff_B.append(temp.count(0))
    
print(min(min(diff_W), min(diff_B)))