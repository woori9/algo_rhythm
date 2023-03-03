from collections import deque
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(maps):
    answer = []
    queue = deque([])
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = 1
                food = 0

                while queue:
                    x, y = queue.popleft()
                    food += int(maps[x][y])

                    for k in range(4):
                        nx, ny = x + d[k][0], y + d[k][1]

                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                            if maps[nx][ny] != 'X' and not visited[nx][ny]:
                                queue.append((nx, ny))
                                visited[nx][ny] = 1

                answer.append(food)

    answer.sort()
    return answer or [-1]
