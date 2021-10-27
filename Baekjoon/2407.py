def factorial(start, end=1):
    res = 1
    while start >= end:
        res *= start
        start -= 1
    return res

n, m = map(int, input().split())

# n! / ((n-m)! * m!)
res = factorial(n, m+1) // factorial(n-m)
print(res)