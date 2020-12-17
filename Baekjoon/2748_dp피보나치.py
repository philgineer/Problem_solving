n = int(input())
dp_arr = [-1 for _ in range(91)]

def fibo(n):
    if dp_arr[n] != -1:
        return dp_arr[n]
    if n == 0:
        dp_arr[n] = 0
    elif n == 1 or n == 2:
        dp_arr[n] = 1
    else:
        dp_arr[n] = fibo(n - 1) + fibo(n - 2)
    return dp_arr[n]

print(fibo(n))