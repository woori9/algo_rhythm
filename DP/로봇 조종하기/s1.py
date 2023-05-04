import sys
sys.stdin = open('input.txt', encoding='UTF8')

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = graph[0][0]

for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + graph[0][j]


for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + graph[i][0]

    from_left = [0] * m
    from_left[0] = dp[i - 1][0] + graph[i][0]

    for j in range(1, m):
        from_left[j] = max(from_left[j - 1] + graph[i][j], dp[i - 1][j] + graph[i][j])

    from_right = [0] * m
    from_right[m - 1] = dp[i - 1][m - 1] + graph[i][m - 1]

    for j in range(m - 2, -1, -1):
        from_right[j] = max(from_right[j + 1] + graph[i][j], dp[i - 1][j] + graph[i][j])

    for j in range(m):
        dp[i][j] = max(from_left[j], from_right[j])

print(dp[n - 1][m - 1])

