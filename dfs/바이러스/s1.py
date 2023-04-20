import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
visited[1] = 1
result = 0

for _ in range(int(input())):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    global result
    result += 1

    for adjacent in graph[node]:
        if not visited[adjacent]:
            visited[adjacent] = 1
            dfs(adjacent)


dfs(1)
print(result - 1)

