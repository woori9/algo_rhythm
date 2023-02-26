import sys
sys.stdin = open('input.txt', encoding='UTF8')


def dfs(item, cost):
    global result

    if cost >= result:
        return

    if item == n:
        result = cost
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(item + 1, cost + graph[item][i])
            visited[i] = 0


for case in range(1, int(input()) + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    result = 99 * n
    dfs(0, 0)
    print('#{} {}'.format(case, result))



