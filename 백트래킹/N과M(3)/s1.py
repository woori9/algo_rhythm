import sys
sys.stdin = open('input.txt', encoding='UTF8')

n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
result = []


def dfs(cnt, current):
    if cnt == m:
        result.append(current[1:])
        return

    for i in range(len(numbers)):
        dfs(cnt+1, current + ' ' + str(numbers[i]))


dfs(0, '')
print(*result, sep='\n')
