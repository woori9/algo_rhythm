import sys
sys.stdin = open('input.txt', encoding='UTF8')

input = sys.stdin.readline

for num in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(e)]
    arr.sort(key=lambda x: x[2])
    root = [i for i in range(v + 1)]
    result = 0

    def find_parent(node):
        if root[node] != node:
            return find_parent(root[node])

        return node


    def union(a, b):
        x, y = find_parent(a), find_parent(b)

        if x == y:
            return False

        if x > y:
            root[y] = x
        else:
            root[x] = y

        return True


    for i in range(len(arr)):
        n1, n2, w = arr[i]
        if union(n1, n2):
            result += w

    print('#{} {}'.format(num, result))
