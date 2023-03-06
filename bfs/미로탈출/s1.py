from collections import deque

d = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def solution(maps):
    n, m = len(maps), len(maps[0])
    result = -1

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
                break

    queue = deque([start])
    visited = [[0] * m for _ in range(n)]
    x, y = start
    visited[x][y] = 1
    visited_lever = False

    while queue:
        x, y = queue.popleft()

        if maps[x][y] == 'L':
            time = visited[x][y] - 1
            visited = [[0] * m for _ in range(n)]
            visited[x][y] = time
            visited_lever = True
            queue.clear()

        elif maps[x][y] == 'E':
            if visited_lever:
                result = visited[x][y]
                break

        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return result
