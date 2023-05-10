import sys, heapq
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

heap = [(0, 1)]
INF = 1e9
distance = [INF] * (n + 1)
distance[1] = 0

while heap:
    dist, node = heapq.heappop(heap)

    if dist > distance[node]:
        continue

    for adjacent in graph[node]:
        adjacent_node, cost = adjacent
        new_dist = max(dist, cost)

        if distance[adjacent_node] > new_dist:
            distance[adjacent_node] = new_dist
            heapq.heappush(heap, (new_dist, adjacent_node))

current = distance[n] + 1

while True:
    if current >= 1000000000:
        break

    for i in range(2, int(current ** (1/2)) + 1):
        if current % i == 0:
            current += 1
            break
    else:
        print(current)
        break


