dp_dict = {0: [1, 0], 1: [0, 1]}

def fibonacci(n):
    if n in dp_dict:
        return dp_dict[n]
    else:
        l1 = fibonacci(n-1)
        l2 = fibonacci(n-2)
        dp_dict[n] = [(a+b) for a, b in zip(l1, l2)]

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2, n+1):
        fibonacci(i)
    print(*dp_dict[n])
