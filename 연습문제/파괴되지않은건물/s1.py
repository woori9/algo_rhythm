def solution(board, skill):
    n, m = len(board), len(board[0])
    sum_accumulated = [[0] * (m + 1) for _ in range(n + 1)]
    answer = 0

    for i in range(len(skill)):
        command, r1, c1, r2, c2, degree = skill[i]
        number = degree if command == 2 else -degree
        sum_accumulated[r1][c1] += number
        sum_accumulated[r2 + 1][c2 + 1] += number
        sum_accumulated[r1][c2 + 1] += -number
        sum_accumulated[r2 + 1][c1] += -number

    for i in range(n):
        for j in range(1, m):
            sum_accumulated[i][j] += sum_accumulated[i][j - 1]

    for i in range(m):
        for j in range(1, n):
            sum_accumulated[j][i] += sum_accumulated[j - 1][i]

    for i in range(n):
        for j in range(m):
            if sum_accumulated[i][j] + board[i][j] > 0:
                answer += 1

    return answer

