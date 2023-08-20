import heapq


def solution(N, road, K):
    answer = 0
    INF = 1e9
    distance = [INF] * N
    graph = [[] for _ in range(N)]
    heap = []

    for i in range(len(road)):
        a, b, c = road[i]
        graph[a - 1].append((b - 1, c))
        graph[b - 1].append((a - 1, c))

    distance[0] = 0
    heapq.heappush(heap, (0, 0))

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > distance[node]:
            continue

        for adjacent_node, time in graph[node]:
            new_cost = distance[node] + time
            if distance[adjacent_node] > new_cost:
                distance[adjacent_node] = new_cost
                heapq.heappush(heap, (new_cost, adjacent_node))

    for dist in distance:
        if dist <= K:
            answer += 1

    return answer

