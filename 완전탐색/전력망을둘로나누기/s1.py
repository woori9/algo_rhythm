def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    result = n

    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)

    for wire in wires:
        visited = [0] * (n + 1)
        cnt = 1
        a, b = wire
        stack = [a]
        visited[a] = 1

        while stack:
            current_node = stack.pop()
            for node in graph[current_node]:
                if node != b and not visited[node]:
                    stack.append(node)
                    visited[node] = 1
                    cnt += 1

        diff = abs(2 * cnt - n)
        if result > diff:
            result = diff

    return result
