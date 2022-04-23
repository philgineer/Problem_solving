import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = [[0] * m for _ in range(n)]
circle = min(n, m) // 2

for _ in range(r):  # 이 for 문 없이, 해당 위치에서 r 만큼 움직일 때의 위치 바로 찾아서 대입
    for c in range(circle):
        for i in range(n):
            for j in range(m):
                # down
                if j == 0+c and -1+c < i < n-1-c:
                    res[i+1][j] = arr[i][j]
                # up
                if j == m-1-c and 0+c < i < n-c:
                    res[i-1][j] = arr[i][j]
                # left
                if i == 0+c and 0+c < j < m-c:
                    res[i][j-1] = arr[i][j]
                # right
                if i == n-1-c and -1+c < j < m-1-c:
                    res[i][j+1] = arr[i][j]
    # update array
    for i in range(n):
        for j in range(m):
            arr[i][j] = res[i][j]
            
# print result
for r in res:
    print(' '.join(map(str, r)))