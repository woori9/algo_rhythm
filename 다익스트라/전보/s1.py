import sys, heapq
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = 1e9
distance = [INF] * (n + 1)
distance[c] = 0
heap = [(0, c)]

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


while heap:
    dist, node = heapq.heappop(heap)

    if dist > distance[node]:
        continue

    for adjacent_node, cost in graph[node]:
        new_value = distance[node] + cost
        if distance[adjacent_node] > new_value:
            distance[adjacent_node] = new_value
            heapq.heappush(heap, (new_value, adjacent_node))

cnt = time = 0

for i in range(1, len(distance)):
    if distance[i] != INF and i != c:
        cnt += 1

    time = max(time, distance[i])

print(cnt, time)
