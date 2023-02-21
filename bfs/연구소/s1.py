import sys
from itertools import combinations

sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

n, m = map(int, input().split())  # 세로, 가로
graph = [list(map(int, input().split())) for _ in range(n)]
virus = []
rooms = []
walls = 0
result = 0


def count_virus(graph):
    cnt = len(virus)

    def spread_virus(x, y):
        nonlocal cnt

        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    cnt += 1
                    spread_virus(nx, ny)

    for v in virus:
        x, y = v
        spread_virus(x, y)

    return cnt


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))

        if graph[i][j] == 0:
            rooms.append((i, j))

        if graph[i][j] == 1:
            walls += 1

for room in combinations(rooms, 3):
    graph_copy = [graph[i][:] for i in range(n)]

    for elememt in room:
        x, y = elememt
        graph_copy[x][y] = 1

    cnt_virus = count_virus(graph_copy)

    safe = n * m - cnt_virus - walls - 3
    if safe > result:
        result = safe

print(result)
