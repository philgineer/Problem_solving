n = int(input())
words = [input() for _ in range(n)]
count = 0
for word in words:
    buff = []
    for i, c in enumerate(word):
        if i == 0:
            buff.append(c)
        elif c == word[i - 1] or c not in buff:
            buff.append(c)
        else:
            continue
    if len(buff) == len(word):
        count += 1
print(count)