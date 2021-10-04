s1 = input()
s2 = input()

common = set(s1).intersection(set(s2))
print('common:', common)

com1 = []
com2 = []
for s, com in zip([s1, s2], [com1, com2]):
    for c in s:
        if c in common:
            com += c

print(com1)
print(com2)

dp