import sys
from itertools import combinations
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken = []
home = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))

        if graph[i][j] == 1:
            home.append((i, j))


result = float('inf')

for element in combinations(chicken, m):
    chicken_distance = 0
    for hx, hy in home:
        min_distance = 2 * n
        for x, y in element:
            min_distance = min(min_distance, abs(x - hx) + abs(y - hy))
        chicken_distance += min_distance

    if result > chicken_distance:
        result = chicken_distance

print(result)
