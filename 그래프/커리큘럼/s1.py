import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
queue = deque([])
time = [0] * (n + 1)
cnt = [0] * (n + 1)
result = [0] * (n + 1)

for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    for j in range(1, len(arr) - 1):
        graph[arr[j]].append(i)
        cnt[i] += 1

    if cnt[i] == 0:
        queue.append(i)
        result[i] = time[i]

while queue:
    node = queue.popleft()

    for adjacent_node in graph[node]:
        cnt[adjacent_node] -= 1
        result[adjacent_node] = max(time[adjacent_node] + result[node], result[adjacent_node])

        if cnt[adjacent_node] == 0:
            queue.append(adjacent_node)

print(*result[1:], sep='\n')

