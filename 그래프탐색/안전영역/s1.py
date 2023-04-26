import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, graph))

result = 1  # rain = 0 일 때
rain = 1

while rain < max_height:
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > rain:
                queue = deque([(i, j)])
                visited[i][j] = 1
                cnt += 1

                while queue:
                    x, y = queue.popleft()

                    for k in range(len(direction)):
                        nx, ny = x + direction[k][0], y + direction[k][1]

                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny] and graph[nx][ny] > rain:
                                visited[nx][ny] = 1
                                queue.append((nx, ny))

    if cnt > result:
        result = cnt

    rain += 1

print(result)
