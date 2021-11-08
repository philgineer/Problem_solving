def go_next(sofar, rest_dict):
    global total
    if not sum(rest_dict.values()):
        total += 1
        return
    for val, cnt in rest_dict.items():
        if cnt and sofar[-1] != val:
            new_dict = rest_dict.copy()
            new_dict[val] -= 1
            go_next(sofar + val, new_dict)

s = input()
total = 0
d = {val: s.count(val) for val in s}
for first in set(s):
    new_dict = d.copy()
    new_dict[first] -= 1
    go_next(first, new_dict)

print(total)