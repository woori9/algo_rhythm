from collections import deque


def solution(info, edges):
    graph = [[] for _ in range(len(info))]

    for edge in edges:
        parent, child = edge
        graph[parent].append(child)

    answer = 0
    queue = deque([(0, 1, 0, graph[0])])
    while queue:
        node, sheep, wolf, next_nodes = queue.popleft()

        if wolf >= sheep:
            continue

        if sheep > answer:
            answer = sheep

        for i in range(len(next_nodes)):
            adjacent_node = next_nodes[i]
            new_next = next_nodes[:i] + next_nodes[i + 1:] + graph[adjacent_node]

            if info[adjacent_node] == 0:
                queue.append((adjacent_node, sheep + 1, wolf, new_next))
            else:
                queue.append((adjacent_node, sheep, wolf + 1, new_next))

    return answer
