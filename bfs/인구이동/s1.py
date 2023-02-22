# 시간초과

import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

from collections import deque
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

while True:
    visited = [[0] * n for _ in range(n)]
    moved = False
    index = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                countries_xy = [(i, j)]
                population = graph[i][j]
                visited[i][j] = 1
                queue = deque([(i, j)])

                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + d[k][0], y + d[k][1]

                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                                queue.append((nx, ny))
                                countries_xy.append((nx, ny))
                                population += graph[nx][ny]
                                visited[nx][ny] = 1

                if len(countries_xy) > 1:
                    moved = True
                    new_population = population // len(countries_xy)

                    for x, y in countries_xy:
                        graph[x][y] = new_population

    if not moved:
        break

    result += 1

print(result)

