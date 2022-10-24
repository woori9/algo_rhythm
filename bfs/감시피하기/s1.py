import sys
from itertools import combinations

sys.stdin = open('input.txt', encoding='UTF8')

input = sys.stdin.readline

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n = int(input())
graph = [input().split() for _ in range(n)]
xys = []
teachers = []
result = 'NO'


def student_searched(x, y):
    for i in range(4):
        nx, ny = x, y
        while 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 'S':
                return True

            if graph[nx][ny] == 'O':
                break

            nx += d[i][0]
            ny += d[i][1]
    return False


for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            xys.append((i, j))

        if graph[i][j] == 'T':
            teachers.append((i, j))


for element in combinations(xys, 3):
    for x, y in element:
        graph[x][y] = 'O'

    for row, col in teachers:
        if student_searched(row, col):
            for x, y in element:
                graph[x][y] = 'X'
            break
    else:
        result = 'YES'
        break

    for x, y in element:
        graph[x][y] = 'X'

print(result)
