n = int(input())
x = []
for _ in range(n):
    x.append(input())
x.sort(key=len)

cnt = n
for i in range(n-1):
    i_len = len(x[i])
    for j in range(i+1, n):
        if x[i] == x[j][:i_len]:
            cnt -= 1
            break
print(cnt)