import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')

input = sys.stdin.readline

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for num in range(1, int(input()) + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for i in range(len(direction)):
            nx, ny = x + direction[i][0], y + direction[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                cost = visited[x][y] + 1
                if graph[nx][ny] > graph[x][y]:
                        cost += graph[nx][ny] - graph[x][y]

                if not visited[nx][ny] or visited[nx][ny] > cost:
                    visited[nx][ny] = cost
                    queue.append((nx, ny))

    print('#{} {}'.format(num, visited[n - 1][n - 1] - 1))
