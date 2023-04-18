import sys
sys.stdin = open('input.txt', encoding='UTF8')
from collections import deque


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + directions[i][0], y + directions[i][1]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == '0':
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

print(visited[n-1][m-1])
