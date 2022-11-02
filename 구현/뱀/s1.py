import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

# X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

# 뱀 1, 사과 2

dx = [0, 1, 0, -1]  # 오 아래 왼 위
dy = [1, 0, -1, 0]

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
graph[0][0] = 1

for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 2

l = int(input())
dict_command = {}
for _ in range(l):
    sec, command = input().split()
    dict_command[int(sec)] = command

result = 0  # 초
i = 0  # 방향
snake = deque([(0, 0)])

while True:
    result += 1
    x_head, y_head = snake[-1]
    nx_head, ny_head = x_head + dx[i], y_head + dy[i]

    if 0 <= nx_head < n and 0 <= ny_head < n:
        if graph[nx_head][ny_head] == 1:
            break

        if graph[nx_head][ny_head] != 2:
            x_tail, y_tail = snake.popleft()
            graph[x_tail][y_tail] = 0
        graph[nx_head][ny_head] = 1
        snake.append((nx_head, ny_head))

        command = dict_command.get(result)

        if command == 'L':
            i = (i - 1) % 4
        if command == 'D':
            i = (i + 1) % 4
    else:
        break

print(result)


