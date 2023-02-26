import sys
sys.stdin = open('input.txt', encoding='UTF8')

d = [(0, 1), (-1, 1), (1, 1)]

for _ in range(int(input())):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    graph = [numbers[i: i+4] for i in range(0, n * m, m)]
    dp = [[0] * m for _ in range(n)]

    for row in range(0, n):
        dp[row][0] = graph[row][0]

    for col in range(0, m - 1):
        for row in range(0, n):
            current = graph[row][col]

            for k in range(3):
                n_row, n_col = row + d[k][0], col + d[k][1]
                if 0 <= n_row < n and 0 <= n_col < m:
                    dp[n_row][n_col] = max(dp[n_row][n_col], dp[row][col] + graph[n_row][n_col])

    result = max([dp[row][m - 1] for row in range(n)])
    print(result)
