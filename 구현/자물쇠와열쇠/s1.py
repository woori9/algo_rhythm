def rotate90Clockwise(arr):
    rotated = [[0] * len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            rotated[i][j] = arr[len(arr) - 1 - j][i]
    return rotated


def is_matched(lock, n):
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    lock_expanded = [[0] * n * 3 for _ in range(n * 3)]

    for i in range(n, 2 * n):  # 범위 설정
        for j in range(n, 2 * n):
            lock_expanded[i][j] = lock[i - n][j - n]

    for i in range(len(lock_expanded) - m):
        for j in range(len(lock_expanded) - m):

            for _ in range(4):
                for a in range(m):
                    for b in range(m):
                        lock_expanded[i + a][j + b] += key[a][b]

                if is_matched(lock_expanded, n):
                    return True

                for a in range(m):
                    for b in range(m):
                        lock_expanded[i + a][j + b] -= key[a][b]

                key = rotate90Clockwise(key)

    return False
