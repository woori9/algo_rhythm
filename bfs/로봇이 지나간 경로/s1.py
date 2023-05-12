import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_shape = ['>', 'v', '<', '^']
a, b = map(int, input().split())
graph = [input().replace('\n', '') for _ in range(a)]
start = None
visited = [[0] * b for _ in range(a)]

for i in range(a):
    if start:
        break

    for j in range(b):
        if graph[i][j] == '#':
            cnt = 0
            idx = -1
            for k in range(len(direction)):
                ni, nj = i + direction[k][0], j + direction[k][1]

                if 0 <= ni < a and 0 <= nj < b:
                    if graph[ni][nj] == '.':
                        cnt += 1
                    else:
                        idx = k
                else:
                    cnt += 1

            if cnt >= 3:
                start = (i, j, idx)
                visited[i][j] = 1
                break

queue = deque([start])
result = ''

while queue:
    x, y, idx = queue.popleft()

    for i in range(len(direction)):
        nx, ny = x + direction[i][0], y + direction[i][1]

        if 0 <= nx < a and 0 <= ny < b:
            if not visited[nx][ny] and graph[nx][ny] == '#':
                visited[nx][ny] = 1
                if idx != i:
                    result = result + 'R' if (idx + 1) % 4 == i else result + 'L'
                result += 'A'
                nx = nx + direction[i][0]
                ny = ny + direction[i][1]
                visited[nx][ny] = 1
                queue.append((nx, ny, i))
                break

print(start[0] + 1, start[1] + 1)
print(direction_shape[start[2]])
print(result)

