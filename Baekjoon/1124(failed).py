import math

def is_prime(num):
    if num in [0, 1]:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def get_primes(num):
    cnt_prime = 0
    i = 2
    while num > 1:
        if num % i == 0:
            num //= i
            cnt_prime += 1
        else:
            i += 1
    return cnt_prime

def is_underprime(num):
    return is_prime(get_primes(num))


a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    cnt += is_underprime(i)
print(cnt)