import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n, m = map(int, input().split())

graph = [input().replace('\n', '') for _ in range(n)]
result = 0


def bfs(i, j):
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    queue = deque([(i, j)])
    largest_distance = 0

    while queue:
        x, y = queue.popleft()

        if visited[x][y] - 1 > largest_distance:
            largest_distance = visited[x][y] - 1

        for k in range(len(direction)):
            nx, ny = x + direction[k][0], y + direction[k][1]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L':
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return largest_distance


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            cnt = 0  # 상 하 좌 우 방면으로 붙어있는 land 개수
            for k in range(len(direction)):
                ni, nj = i + direction[k][0], j + direction[k][1]

                if 0 <= ni < n and 0 <= nj < m:
                    if graph[ni][nj] == 'L':
                        cnt += 1

            if cnt == 1 or cnt == 2:
                largest_distance = bfs(i, j)

                if largest_distance > result:
                    result = largest_distance

print(result)
