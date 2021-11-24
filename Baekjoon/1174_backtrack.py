def backtrack(num):
    table.append(int(num))
    for next_digit in range(0, int(num[-1])):
        backtrack(num + str(next_digit))


n = int(input())
if n > 1023:
    print(-1)
else:
    table = []
    for first_digit in range(10):
        backtrack(str(first_digit))
    print(sorted(table)[n-1])