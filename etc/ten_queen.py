total_number = 0 # 전체 경우의 수

def print_map(map):
    for i in range(10):
        print(map[i], end='')
    print('')
    global total_number
    total_number += 1
    
def is_invalid(buf_map, count, j):
    # 같은 줄
    if buf_map[count] == buf_map[j]:
        return 1
    # 대각선
    if count - j == buf_map[count] - buf_map[j]:
        return 1
    # 대각선 반대방향
    if count - j == - buf_map[count] + buf_map[j]:
        return 1
    return 0
    
def place_queen(map, count):
    if count == 10:
        print_map(map)
        # valid한 맵을 print 후, 다음 가능한 맵을 탐색하기 위해 (필요시 연달아) return을 사용해 재귀를 빠져나감
        return
    # 해당 재귀의 버퍼맵을 따로 생성 후 저장
    buf_map = [0 for i in range(10)]
    for i in range(10):
        buf_map[i] = map[i]
    for i in range(10):
        buf_map[count] = i
        j = 0
        while j < count:
            if (is_invalid(buf_map, count, j)):
                break
            j += 1
        # valid 한 경우에만 다음 재귀로
        if j == count:
            place_queen(buf_map, count + 1)
            
def ft_ten_queen():
    global total_number
    total_number = 0
    map_init = [0 for i in range(10)]
    count = 0
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 으로 시작함
    place_queen(map_init, count)
    return total_number

ft_ten_queen()
print("Total number: ", total_number)