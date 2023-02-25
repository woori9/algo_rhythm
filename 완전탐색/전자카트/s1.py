import sys
from itertools import permutations
sys.stdin = open('input.txt', encoding='UTF8')

for case in range(1, int(input()) + 1):
    n = int(input())
    rooms = [num for num in range(2, n + 1)]
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = 100 * n

    for order in permutations(rooms):
        value = graph[0][order[0] - 1]
        for j in range(len(order)):
            if j == len(order) - 1:
                value += graph[order[j] - 1][0]
            else:
                value += graph[order[j] - 1][order[j + 1] - 1]

        if result > value:
            result = value

    print('#{} {}'.format(case, result))



