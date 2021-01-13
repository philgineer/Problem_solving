m = int(input())
n = int(input())

def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

total = 0
mini = n
for num in range(m, n + 1):
    if is_prime(num):
        total += num
        if num < mini:
            mini = num
if total > 0:
    print(total)
    print(mini)
else:
    print(-1)