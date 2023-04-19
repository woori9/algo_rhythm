import sys
sys.stdin = open('input.txt', encoding='UTF8')

import heapq

input = sys.stdin.readline
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = 1e9

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(n, start):
    heap = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        dist, node = heapq.heappop(heap)

        if distance[node] < dist:
            continue

        for element in graph[node]:
            adjacent, cost = element
            new_dist = distance[node] + cost

            if distance[adjacent] > new_dist:
                distance[adjacent] = new_dist
                heapq.heappush(heap, (new_dist, adjacent))

    return distance


d1 = dijkstra(n, 1)
d2 = dijkstra(n, v1)
d3 = dijkstra(n, n)

path1 = (d1[v1], d2[v2], d3[v2])
path2 = (d1[v2], d2[v2], d3[v1])

if INF in path1 or INF in path2:
    print(-1)
else:
    print(min(sum(path1), sum(path2)))
