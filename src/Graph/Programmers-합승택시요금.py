import heapq
import sys

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  
      # 현재 노드가 이미 처리된 노드라면 
      # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return distances

def solution(n, s, a, b, fares):
    graph = {}
    for i  in range(1, n+1):
        graph[i] = {}

    for fare in fares:
        tmp = graph[fare[0]]
        tmp[fare[1]] = fare[2]
        tmp2 = graph[fare[1]]
        tmp2[fare[0]] = fare[2]
        graph[fare[0]] = tmp
        graph[fare[1]] = tmp2

    min_v = sys.maxsize
    for w in range(1,n+1):
        w_dist = dijkstra(graph, s)[w]
        a_dist = dijkstra(graph, w)[a]
        b_dist = dijkstra(graph, w)[b]
        sum = w_dist + a_dist + b_dist
        if sum < min_v:
            min_v = sum
    return min_v