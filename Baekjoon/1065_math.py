n = int(input())
cnt = 0
for num in range(n, 0, -1):
    num_list = list(map(int, str(num)))
    flag = 1
    diff = []
    for i in range(len(num_list) - 1):
        diff.append(num_list[i] - num_list[i+1])
    for d in diff:
        if d != diff[0]:
            flag = 0
    cnt += flag
print(cnt)