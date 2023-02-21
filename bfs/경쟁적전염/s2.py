import sys
sys.stdin = open('input.txt', encoding='UTF8')

from collections import deque
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
virus = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j, 0))

virus.sort(key=lambda x: x[0])

queue = deque(virus)

while queue:
    v, v_x, v_y, sec = queue.popleft()

    for i in range(4):
        nx, ny = v_x + d[i][0], v_y + d[i][1]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0 and sec < s:
                graph[nx][ny] = v
                queue.append((v, nx, ny, sec + 1))

print(graph[x-1][y-1])
