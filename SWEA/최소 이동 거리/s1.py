import sys
import heapq
sys.stdin = open('input.txt', encoding='UTF8')

input = sys.stdin.readline
INF = 1e9

for num in range(1, int(input()) + 1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    distance[0] = 0
    heap = [(0, 0)]

    for i in range(e):
        s, e, cost = map(int, input().split())
        graph[s].append((e, cost))

    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distance[node]:
            continue

        for element in graph[node]:
            adjacent_node, cost = element
            new_distance = dist + cost

            if distance[adjacent_node] > new_distance:
                distance[adjacent_node] = new_distance
                heapq.heappush(heap, (new_distance, adjacent_node))

    print('#{} {}'.format(num, distance[n]))
