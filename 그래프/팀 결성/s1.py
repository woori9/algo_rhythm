import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


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
    command, a, b = map(int, input().split())

    if command == 0:
        union(a, b)

    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
