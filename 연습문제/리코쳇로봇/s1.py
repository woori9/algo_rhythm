from collections import deque
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solution(board):
    n, m = len(board), len(board[0])
    visited = [[0] * m for _ in range(n)]
    answer = -1
    start = None

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
                visited[i][j] = 1
                break

    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        if board[x][y] == 'G':
            answer = visited[x][y] - 1
            break

        for i in range(4):
            nx, ny = x, y

            while True:
                temp_x, temp_y = nx + d[i][0], ny + d[i][1]
                if not (0 <= temp_x < n and 0 <= temp_y < m) or board[temp_x][temp_y] == 'D':
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
                    break

                nx, ny = temp_x, temp_y

    return answer
