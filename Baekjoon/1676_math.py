import sys

def count_zero(num):
    global zero, two, five
    if num % 10 == 0:
        cnt = 0
        s = str(i)
        for j in range(len(s)-1, 0, -1):
            if s[j] == '0':
                cnt += 1
            else:
                break
        zero += cnt
        num //= 10 ** cnt
    while num % 2 == 0:
        two += 1
        num //= 2
    while num % 5 == 0:
        five += 1
        num //= 5

n = int(sys.stdin.readline())
zero, two, five = 0, 0, 0
for i in range(n, 0, -1):
    count_zero(i)
print(min(five, two) + zero)