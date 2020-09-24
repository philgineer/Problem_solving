import sys
input = sys.stdin.readline
INF = int(1e9) # 10억을 무한으로 설정

# 노드 개수, 간선 개수, 시작노드 입력받기
n, m = map(int, input().split())
start = int(input())

# 그래프 리스트, 방문 체크 리스트, 최단 거리 테이블 초기화
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    # a 노드에서 b 노드로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    # 시작노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내 방문 처리
        now = get_smallest_node()
        visited[now] = True
        
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    if distance[i] = INF:
        print('INF')
    else:
        print(distance[i])