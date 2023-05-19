import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
roads = []


def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union(node1, node2):
    a = find_parent(node1)
    b = find_parent(node2)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    a, b, c = map(int, input().split())
    roads.append((c, a, b))
roads.sort()

result = v = 0

for i in range(m):
    c, a, b = roads[i]

    if find_parent(a) != find_parent(b):
        union(a, b)
        v += 1
        result += c

    if v == n - 2:
        break

print(result)
