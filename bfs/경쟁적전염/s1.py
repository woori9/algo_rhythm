import sys
sys.stdin = open('input.txt', encoding='UTF8')

from collections import deque
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
virus_xy = []

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            virus_xy.append((0, graph[i][j], i, j))

virus_xy.sort(key=lambda x: x[1])
queue = deque(virus_xy)

while queue:
    sec, virus, row, col = queue.popleft()

    if sec == s:
        break

    for i in range(4):
        nx, ny = row + directions[i][0], col + directions[i][1]

        if 0 <= nx < n and 0 <= ny < n:
            if not graph[nx][ny]:
                graph[nx][ny] = virus
                queue.append((sec + 1, virus, nx, ny))

print(graph[x - 1][y - 1])


