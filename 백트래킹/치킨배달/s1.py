import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken = []
home = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))

        if graph[i][j] == 1:
            home.append((i, j))

chicken_distance = [n*2 for _ in range(len(home))]
result = sum(chicken_distance)


def dfs(idx, cnt, chicken_distance):
    global result

    if cnt == m:
        if result > sum(chicken_distance):
            result = sum(chicken_distance)
        return

    for i in range(idx, len(chicken)):
        copy = chicken_distance[:]
        for j in range(len(home)):
            distance = abs(chicken[i][0] - home[j][0]) + abs(chicken[i][1] - home[j][1])
            copy[j] = min(chicken_distance[j], distance)

        dfs(i + 1, cnt + 1, copy)


dfs(0, 0, chicken_distance)
print(result)
