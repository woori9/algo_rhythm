import sys
from collections import deque
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k, x = map(int, input().split())
    dict_road = {}
    visited = [0] * (n + 1)
    result = []

    for _ in range(m):
        a, b = map(int, input().split())
        roads_a = dict_road.get(a, [])
        roads_a.append(b)
        dict_road[a] = roads_a

    queue = deque([])
    queue.append((x, 0))
    visited[x] = 1

    while queue:
        node, distance = queue.popleft()
        roads = dict_road.get(node, [])

        if distance == k:
            result.append(node)
            continue

        for road in roads:
            if not visited[road]:
                visited[road] = 1
                queue.append((road, distance + 1))

    if result:
        result.sort()
        for element in result:
            print(element)
    else:
        print(-1)
