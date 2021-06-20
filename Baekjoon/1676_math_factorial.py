def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

n = int(input())
s = str(factorial(n))
cnt = 0
i = len(s) - 1
while s[i] == '0':
    cnt += 1
    i -= 1
print(cnt)