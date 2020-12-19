k = int(input())
stack = []
res = 0
for _ in range(k):
    new_num = int(input())
    if new_num == 0:
        res -= stack[-1]
        stack.pop()
    else:
        stack.append(new_num)
        res += stack[-1]
print(res)
        
    