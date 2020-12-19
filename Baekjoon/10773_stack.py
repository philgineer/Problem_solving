k = int(input())
stack = []
for _ in range(k):
    new_num = input()
    if new_num == "0":
        stack.pop()
    else:
        stack.append(int(new_num))
res = 0
for num in stack:
    res += num
print(res)