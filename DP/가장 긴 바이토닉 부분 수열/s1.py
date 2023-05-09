import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())
arr = list(map(int, input().split()))
dp1 = [1] * n
dp2 = [1] * n

for i in range(0, n):
    for j in range(i + 1, n):
        if arr[j] > arr[i]:
            dp1[j] = max(dp1[i] + 1, dp1[j])

for i in range(n - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if arr[j] > arr[i]:
            dp2[j] = max(dp2[i] + 1, dp2[j])

result = 1
for i in range(n):
    if dp1[i] + dp2[i] - 1 > result:
        result = dp1[i] + dp2[i] - 1

print(result)
