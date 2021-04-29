pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

def dist(pos1, pos2):
    for i in range(4):
        for j in range(3):
            if pos1 == pad[i][j]:
                row1, col1 = i, j

    for i in range(4):
        for j in range(3):
            if pos2 == pad[i][j]:
                row2, col2 = i, j
    
    distance = abs(row2 - row1) + abs(col2 - col1)
    # print('dist bw', pos1, 'and', pos2, '=', distance)
    
    return distance

def solution(numbers, hand):
    left_pos = '*'
    right_pos = '#'
    answer = ""

    for num in numbers:
        if num in [1, 4, 7]:
            res = 'L'
            left_pos = num
        elif num in [3, 6, 9]:
            res = 'R'
            right_pos = num
        elif dist(num, left_pos) == dist(num, right_pos):
            if hand == 'right':
                res = 'R'
                right_pos = num
            else:
                res = 'L'
                left_pos = num
        elif dist(num, left_pos) > dist(num, right_pos):
            res = 'R'
            right_pos = num
        else:
            res = 'L'
            left_pos = num

        answer += res
    
    return answer


result = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
print(result)
print("LRLLLRLLRRL")