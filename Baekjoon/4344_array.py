c = int(input())
res = []
for i in range(c):
    case = list(map(int, input().split()))
    n = case.pop(0)
    avg = sum(case) / n
    cnt = 0
    for student in case:
        if student > avg:
            cnt += 1
    res.append('{:.3f}%'.format(cnt * 100 / n))
for r in res:
    print(r)