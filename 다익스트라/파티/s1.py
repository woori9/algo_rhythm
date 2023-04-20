import sys
import heapq

sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

n, e, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = 1e9

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start, end=0):
    heap = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        dist, node = heapq.heappop(heap)

        if distance[node] < dist:
            continue

        if node == end:
            return distance

        for element in graph[node]:
            adjacent, cost = element
            new_dist = distance[node] + cost

            if distance[adjacent] > new_dist:
                distance[adjacent] = new_dist
                heapq.heappush(heap, (new_dist, adjacent))

    return distance


result = [0] * (n + 1)
back_distance = dijkstra(x)
back_distance[0] = 0

for i in range(1, n + 1):
    dist = dijkstra(i, x)
    result[i] = back_distance[i] + dist[x]

print(max(result))
