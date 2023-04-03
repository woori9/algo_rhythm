import sys

sys.setrecursionlimit(100000)


def solution(n, lighthouse):
    graph = [[] for _ in range(n + 1)]
    tree = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    result = 0

    for i in range(len(lighthouse)):
        a, b = lighthouse[i]
        graph[a].append(b)
        graph[b].append(a)

    def build_tree(node):
        for element in graph[node]:
            if not visited[element]:
                visited[element] = 1
                tree[node].append(element)
                build_tree(element)

    visited[1] = 1
    build_tree(1)

    def dfs(node):
        nonlocal result

        if not tree[node]:  # leaf
            return 0

        lightened_child = 0

        for child in tree[node]:
            lightened_child += dfs(child)

        if lightened_child == len(tree[node]):  # 모든 자식 노드가 불을 킴
            return 0

        result += 1
        return 1

    visited[1] = 1
    dfs(1)
    return result
