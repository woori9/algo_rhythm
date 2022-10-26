import sys
sys.stdin = open('input.txt', encoding='UTF8')

x = int(input())

dp = [0] * 30001

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[x])
