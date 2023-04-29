import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

l, c = map(int, input().split())
arr = input().split()
arr.sort()
result = []


def dfs(idx, value, left, vowels):
    if left > (c - idx):
        return

    if left == 0:
        if vowels > 0 and (l - vowels) > 1:
            result.append(value)
        return

    for i in range(idx, len(arr)):
        dfs(i + 1, value + arr[i], left - 1, vowels + 1 if (arr[i] in ('a', 'e', 'i', 'o', 'u')) else vowels)


dfs(0, '', l, 0)

print(*result, sep='\n')
