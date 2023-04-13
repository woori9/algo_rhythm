from collections import deque


def solution(n, roads, sources, destination):
    visited = [0] * (n + 1)
    visited[destination] = 1
    graph = [[] for _ in range(n + 1)]

    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([(destination)])

    while queue:
        location = queue.popleft()
        dist = visited[location]

        for element in graph[location]:
            if not visited[element]:
                visited[element] = dist + 1
                queue.append((element))

    result = [0] * len(sources)

    for i in range(len(sources)):
        result[i] = visited[sources[i]] - visited[destination]

    return result

