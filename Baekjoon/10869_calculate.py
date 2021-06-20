a, b = input().split()
for cal in ['+', '-', '*', '//', '%']:
    print(eval(a + cal + b))