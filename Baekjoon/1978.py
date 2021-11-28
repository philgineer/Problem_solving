n = int(input())
num_list = list(map(int, input().split()))
count = 0

def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

for num in num_list:
    if is_prime(num):
        count += 1
print(count)