import sys
sys.stdin = open('input.txt', encoding='UTF8')

n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
result = []


def dfs(cnt, idx, current):
    if cnt == m:
        result.append(current[1:])
        return

    for i in range(idx, len(numbers)):
        dfs(cnt+1, i, current + ' ' + str(numbers[i]))


dfs(0, 0, '')
print(*result, sep='\n')
