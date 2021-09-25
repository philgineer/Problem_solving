import sys
input = sys.stdin.readline

def sort_idx(input_list):
    return sorted(range(3), key=input_list.__getitem__)

def shift_dp(table):
    table[0] = table[1]
    table[1] = table[2]
    table[2] = 0

def shift_everything():
    for i in range(3):
        # shift graph
        graph[0][i] = graph[1][i]
        graph[1][i] = graph[2][i]
        # shift sort idx list
        prev_idx[i] = curr_idx[i]
    # shift dp list
    shift_dp(dp_max)
    shift_dp(dp_min)


n = int(input())
# [two steps before, last, current]
graph = [[0, 0, 0] for _ in range(3)]
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]

for iteration in range(n):
    graph[2] = list(map(int, input().split()))
    curr_idx = sort_idx(graph[2])

    if iteration == 0:
        prev_idx = sort_idx(graph[2])
        dp_max[2] = graph[2][curr_idx[2]]
        dp_min[2] = graph[2][curr_idx[0]]
        
        shift_everything()
        print('max: ',dp_max)
        continue

    # calculate dp_max
    if abs(curr_idx[2] - prev_idx[2]) == 2:
        temp = graph[1][prev_idx[1]] + graph[2][curr_idx[2]]
        if graph[1][prev_idx[2]] + graph[2][curr_idx[1]] > temp:
            dp_max[2] = dp_max[0] + graph[1][prev_idx[2]] + graph[2][curr_idx[1]]
            #curr_idx[1], curr_idx[2] = curr_idx[2], curr_idx[1]
        else:
            dp_max[2] = dp_max[0] + temp
    else:
        dp_max[2] = dp_max[1] + graph[2][curr_idx[2]]

    # calculate dp_min
    if abs(curr_idx[0] - prev_idx[0]) == 2:
        temp = graph[1][prev_idx[1]] + graph[2][prev_idx[0]]
        if graph[1][prev_idx[0]] + graph[2][curr_idx[1]] < temp:
            dp_min[2] = dp_min[0] + graph[1][prev_idx[0]] + graph[2][curr_idx[1]]
            #curr_idx[0], curr_idx[1] = curr_idx[1], curr_idx[0]
        else:
            dp_min[2] = dp_min[0] + temp
    else:
        dp_min[2] = dp_min[1] + graph[2][curr_idx[0]]

    # update dp table (store recent 3 values)
    shift_everything()

    print('max:', dp_max)
    #print('min:', dp_min)

print(dp_max[1], dp_min[1])