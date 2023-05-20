import sys
sys.stdin = open('input.txt', encoding='UTF8')

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
current = 1  # current - 1 까지 만들 수 있다고 가정

for i in range(n):
    if arr[i] > current:
        break

    current += arr[i]

print(current)
