import sys
sys.stdin = open('input.txt', encoding='UTF8')

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = cnt = 0

for i in range(len(arr)):
    cnt += 1
    if cnt == arr[i]:
        result += 1
        cnt = 0

print(result)
