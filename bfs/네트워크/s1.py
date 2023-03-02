from collections import deque


def solution(n, computers):
    result = 0
    visited = [0] * n
    queue = deque([])

    for i in range(n):
        if not visited[i]:
            queue.append(i)
            visited[i] = 1
            result += 1

            while queue:
                node = queue.popleft()

                for i in range(n):
                    if i == node:
                        continue

                    if not visited[i] and computers[node][i]:
                        visited[i] = 1
                        queue.append(i)
    return result
