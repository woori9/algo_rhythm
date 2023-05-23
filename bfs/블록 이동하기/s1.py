from collections import deque

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution(board):
    n = len(board)
    visited = set([(0, 0, 0, 1)])
    queue = deque([(0, 0, 0, 1, 0)])
    result = 1e9

    def make_horizontal(x, y1, y2, sec):
        if 0 <= x - 1 < n:  # 윗열 확인
            if board[x - 1][y1] == 0 and board[x - 1][y2] == 0:
                xy = (x - 1, y1, x, y1)
                if xy not in visited:
                    visited.add((x - 1, y1, x, y1))
                    queue.append((x - 1, y1, x, y1, sec + 1))

                xy = (x - 1, y2, x, y2)
                if xy not in visited:
                    visited.add((x - 1, y2, x, y2))
                    queue.append((x - 1, y2, x, y2, sec + 1))

        if 0 <= x + 1 < n:
            if board[x + 1][y1] == 0 and board[x + 1][y2] == 0:
                xy = (x, y1, x + 1, y1)
                if xy not in visited:
                    visited.add((x, y1, x + 1, y1))
                    queue.append((x, y1, x + 1, y1, sec + 1))

                xy = (x, y2, x + 1, y2)
                if xy not in visited:
                    visited.add((x, y2, x + 1, y2))
                    queue.append((x, y2, x + 1, y2, sec + 1))

    def make_vertical(y, x1, x2, sec):
        if 0 <= y - 1 < n:  # 왼쪽 행 확인
            if board[x1][y - 1] == 0 and board[x2][y - 1] == 0:
                xy = (x1, y - 1, x1, y)
                if xy not in visited:
                    visited.add((x1, y - 1, x1, y))
                    queue.append((x1, y - 1, x1, y, sec + 1))

                xy = (x2, y - 1, x2, y)
                if xy not in visited:
                    visited.add((x2, y - 1, x2, y))
                    queue.append((x2, y - 1, x2, y, sec + 1))

        if 0 <= y + 1 < n:
            if board[x1][y + 1] == 0 and board[x2][y + 1] == 0:
                xy = (x1, y, x1, y + 1)
                if xy not in visited:
                    visited.add((x1, y, x1, y + 1))
                    queue.append((x1, y, x1, y + 1, sec + 1))

                xy = (x2, y, x2, y + 1)
                if xy not in visited:
                    visited.add((x2, y, x2, y + 1))
                    queue.append((x2, y, x2, y + 1, sec + 1))

    while queue:
        x1, y1, x2, y2, sec = queue.popleft()

        if (x1 == y1 == n - 1) or (x2 == y2 == n - 1):
            result = sec
            break

        for i in range(len(d)):
            n_x1, n_y1 = x1 + d[i][0], y1 + d[i][1]
            n_x2, n_y2 = x2 + d[i][0], y2 + d[i][1]

            if 0 <= n_x1 < n and 0 <= n_y1 < n and board[n_x1][n_y1] == 0:
                if 0 <= n_x2 < n and 0 <= n_y2 < n and board[n_x2][n_y2] == 0:
                    if (n_x1, n_y1, n_x2, n_y2) not in visited:
                        visited.add((n_x1, n_y1, n_x2, n_y2))
                        queue.append((n_x1, n_y1, n_x2, n_y2, sec + 1))

        if x1 == x2:  # 수평
            make_horizontal(x1, y1, y2, sec)
        else:
            make_vertical(y1, x1, x2, sec)

    return result
