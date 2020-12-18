n = int(input())

def print_prime(num, i):
    if num == 1:
        return
    while num > 1:
        if num % i == 0:
            print(i)
            num /= i
        else:
            i += 1
        
print_prime(n, 2)