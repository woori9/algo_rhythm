import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = 1e9

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
fish = [[] for _ in range(7)]
shark = 2
cnt_eat = 0
result = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0
        elif graph[i][j]:
            fish[graph[i][j]].append((i, j))

can_eat = fish[1][:]

while can_eat:
    visited = [[0] * n for _ in range(n)]
    visited[now_x][now_y] = 1
    queue = deque([(now_x, now_y)])
    shortest_distance = INF
    next_xy = []

    while queue:
        x, y = queue.popleft()

        if shortest_distance < visited[x][y] - 1:
            break

        if (x, y) in can_eat:
            shortest_distance = visited[x][y] - 1
            next_xy.append((x, y))

        for i in range(len(direction)):
            nx, ny = x + direction[i][0], y + direction[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] <= shark:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    if not next_xy:
        break

    next_xy.sort(key=lambda x: (x[0], x[1]))
    idx = can_eat.index((next_xy[0]))
    now_x, now_y = can_eat.pop(idx)
    cnt_eat += 1
    result += shortest_distance

    if cnt_eat == shark:
        if shark < 7:
            can_eat.extend(fish[shark])
        shark += 1
        cnt_eat = 0

print(result)

