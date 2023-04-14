import heapq


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    intensities = [10000001] * (n + 1)
    heap = []

    for i in range(len(paths)):
        a, b, cost = paths[i]
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    for i in range(len(gates)):
        heap.append((0, gates[i]))
        intensities[gates[i]] = 0

    answer = [-1, 10000001]

    while heap:
        intensity, node = heapq.heappop(heap)

        if intensity > answer[1]:
            break

        if intensity > intensities[node]:
            continue

        if node in summits:
            if intensity < answer[1]:
                answer = [node, intensity]
            if node < answer[0]:
                answer[0] = node
            continue

        for element in graph[node]:
            adjacent_node, cost = element
            new_intensity = max(intensities[node], cost)

            if intensities[adjacent_node] > new_intensity:
                intensities[adjacent_node] = new_intensity
                heapq.heappush(heap, (new_intensity, adjacent_node))

    return answer
