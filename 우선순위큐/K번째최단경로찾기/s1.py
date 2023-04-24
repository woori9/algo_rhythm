import sys
import heapq
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = [-1] * (n + 1)
INF = 1e9

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra():
    distance = [[INF] * k for _ in range(n + 1)]
    distance[1][0] = 0
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        cost, node = heapq.heappop(heap)

        # 처음에 >= 를 썼다가 실패.
        # 다른 경로지만 지금까지의 cost가 같은 경우 인접 노드의 값을 갱신할 수도 있다.
        if cost > distance[node][-1]:
            continue

        for element in graph[node]:
            adjacent_node, time = element
            new_distance = cost + time
            current_distance = distance[adjacent_node]

            if current_distance[-1] > new_distance:
                current_distance[-1] = new_distance
                current_distance.sort()
                heapq.heappush(heap, (new_distance, adjacent_node))

    return distance


distance = dijkstra()
result = list(map(lambda x: x[-1] if x[-1] != INF else -1, distance[1:]))

print(*result, sep='\n')
