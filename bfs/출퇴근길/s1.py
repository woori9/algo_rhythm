# !오답

import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

n, m = map(int, input().split())
graph_original = [[] for _ in range(n + 1)]
graph_reversed = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph_original[x].append(y)
    graph_reversed[y].append(x)

s, t = map(int, input().split())


def bfs(start, end, graph):
    queue = deque([start])
    visited = [0] * (n + 1)
    visited[start] = 1

    while queue:
        node = queue.popleft()

        if node == end:
            continue

        for adjacent_node in graph[node]:
            if not visited[adjacent_node]:
                visited[adjacent_node] = 1
                queue.append(adjacent_node)

    return visited


a = bfs(s, t, graph_original)
d = bfs(t, s, graph_reversed)
b = bfs(s, t, graph_reversed)
c = bfs(t, s, graph_original)

result = 0
print(a, b, c, d)
for i in range(1, n + 1):
    if (i == s) or (i == t):
        continue

    if a[i] and b[i] and c[i] and d[i]:
        result += 1

print(result)
