res = []
command_list = []

n = int(input())
for i in range(n):
    command_list.append(input())

for command in command_list:
    if command.split()[0] == "push":
        res.append(int(command.split()[1]))
    elif command.split()[0] == "pop":
        if res:
            print(res.pop())
        else:
            print(-1)
    elif command.split()[0] == "size":
        print(len(res))
    elif command.split()[0] == "empty":
        if res:
            print(0)
        else:
            print(1)
    elif command.split()[0] == "top":
        if res:
            print(res[-1])
        else:
            print(-1)