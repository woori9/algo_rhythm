dict_direction = {
    'N': (-1, 0),
    'S': (1, 0),
    'W': (0, -1),
    'E': (0, 1),
}


def solution(park, routes):
    n, m = len(park), len(park[0])

    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x, y = i, j
                break

    for route in routes:
        direction, move = route.split()
        move = int(move)
        d = dict_direction.get(direction)
        nx, ny = x, y

        while move:
            nx += d[0]
            ny += d[1]
            move -= 1

            if not (0 <= nx < n and 0 <= ny < m):
                break

            if park[nx][ny] == 'X':
                break
        else:
            x, y = nx, ny

    return [x, y]
