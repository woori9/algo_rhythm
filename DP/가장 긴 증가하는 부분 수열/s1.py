import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(0, n):
    for j in range(i + 1, n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i] + 1)


print(max(dp))
