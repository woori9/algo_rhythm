import sys
sys.stdin = open('input.txt', encoding='UTF8')


# 오답

for case in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    root = [i for i in range(n + 1)]
    arr = list(map(int, input().split()))


    def find(node):
        if root[node] == node:
            return node

        root[node] = find(root[node])
        return root[node]


    def union(a, b):
        x = find(a)
        y = find(b)

        if x < y:
            root[y] = x
        else:
            root[x] = y


    for i in range(0, len(arr), 2):
        union(arr[i], arr[i + 1])

    result = len(set(root)) - 1
    print('#{} {}'.format(case, result))
