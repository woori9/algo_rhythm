import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]


def lower_bound(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if dp[mid] == target:
            return

        if dp[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    if start <= len(dp) - 1:
        dp[start] = target


for i in range(1, n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])

    if dp[-1] > arr[i]:
        lower_bound(0, len(dp) - 1, arr[i])

print(len(dp))
