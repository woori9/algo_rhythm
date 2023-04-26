import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
queue = deque([(a, 0)])
result = -1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


while queue:
    person, cnt = queue.popleft()

    if person == b:
        result = cnt
        break

    for adjacent in graph[person]:
        if not visited[adjacent]:
            visited[adjacent] = 1
            queue.append((adjacent, cnt + 1))

print(result)
