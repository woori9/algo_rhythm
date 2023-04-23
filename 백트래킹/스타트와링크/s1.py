import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
visited[0] = 1
result = 100 * n
# 123456
# 123 124 125 126 134 135 136 145 146 156
# 456 356 346 345 256 246 245 236 235 234


def dfs(idx, team, value):
    global result

    if len(team) == n // 2:
        other_team = []
        other_value = 0
        for i in range(len(visited)):
            if not visited[i]:
                for member in other_team:
                    other_value += graph[i][member] + graph[member][i]
                other_team.append(i)
        diff = abs(value - other_value)
        if result > diff:
            result = diff
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            n_value = value
            for member in team:
                n_value += graph[member][i] + graph[i][member]
            dfs(i, team + [i], n_value)
            visited[i] = 0


dfs(1, [0], 0)
print(result)
