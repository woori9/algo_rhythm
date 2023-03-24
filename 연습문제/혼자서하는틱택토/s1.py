def solution(board):
    o_cnt = x_cnt = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_cnt += 1
            if board[i][j] == 'X':
                x_cnt += 1

    if x_cnt > o_cnt or abs(x_cnt - o_cnt) > 1:
        return 0

    def is_win(element):
        cross1_win = True
        cross2_win = True

        for i in range(3):
            horizontal_win = True
            vertical_win = True
            for j in range(3):
                if board[i][j] != element:
                    horizontal_win = False

                if board[j][i] != element:
                    vertical_win = False

            if horizontal_win or vertical_win:
                return True

            if element != board[i][i]:
                cross1_win = False

            if element != board[i][2 - i]:
                cross2_win = False

        if cross1_win or cross2_win:
            return True
        return False

    win_0 = is_win('O')
    win_X = is_win('X')
    if win_0 and win_X:
        return 0

    if win_0 and x_cnt >= o_cnt:
        return 0

    if win_X and o_cnt > x_cnt:
        return 0

    return 1

