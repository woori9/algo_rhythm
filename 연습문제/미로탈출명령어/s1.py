import sys
sys.setrecursionlimit(3000)

dict_d = {
    'l': (0, -1),
    'r': (0, 1),
    'u': (-1, 0),
    'd': (1, 0)
}


def solution(n, m, x, y, r, c, k):
    distance = abs(x - r) + abs(y - c)
    if distance > k or (k - distance) % 2:
        return 'impossible'

    result = ''

    def dfs(location, k, current):
        nonlocal result
        x, y = location

        if abs(x - r) + abs(y - c) > k:
            return

        if k == 0:
            if location == (r, c):
                result = current
            return

        for direction in ['d', 'l', 'r', 'u']:
            move = dict_d.get(direction)
            nx, ny = x + move[0], y + move[1]

            if (1 <= nx <= n) and (1 <= ny <= m):
                if not result:
                    dfs((nx, ny), k - 1, current + direction)

    dfs((x, y), k, '')
    return result
