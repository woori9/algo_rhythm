import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
graph = [input().replace('\n', '') for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0] = [1, 1]
queue = deque([(0, 0, 0)])

while queue:
    x, y, z = queue.popleft()

    for i in range(4):
        nx, ny = x + direction[i][0], y + direction[i][1]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny][z]:
                if graph[nx][ny] == '0':
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))

                elif graph[nx][ny] == '1' and z == 0:  # z = 0: 벽 안 부숨
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        queue.append((nx, ny, 1))

r1, r2 = visited[n-1][m-1]
result = min(r1, r2) if (not 0 in visited[n-1][m-1]) else (r1 or r2)
print(result or -1)

