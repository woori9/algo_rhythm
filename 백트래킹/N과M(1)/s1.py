import sys
sys.stdin = open('input.txt', encoding='UTF8')

n, m = map(int, input().split())
visited = [0] * (n + 1)
numbers = [i for i in range(1, n + 1)]
result = []


def dfs(cnt, current):

    if cnt == m:
        result.append(current[1:])
        return

    for i in range(len(numbers)):
        if not visited[numbers[i]]:
            visited[numbers[i]] = 1
            dfs(cnt+1, current + ' ' + str(numbers[i]))
            visited[numbers[i]] = 0


dfs(0, '')
print(*result, sep='\n')
