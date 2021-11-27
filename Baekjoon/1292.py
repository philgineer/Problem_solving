a, b = map(int, input().split())

cnt = 0
acc = 0
for i in range(b + 1):
    for _ in range(i):
        cnt += 1
        if cnt >= a and cnt <=b:
            acc += i

print(acc)