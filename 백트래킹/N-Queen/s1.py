def solution(n):
    answer = 0
    rows = [0] * n

    def dfs(x):
        nonlocal answer

        if x == n:
            answer += 1
            return

        for col in range(n):
            rows[x] = col

            for idx in range(x):  # 지금까지 기록된 rows 탐색
                if rows[idx] == col or abs(rows[idx] - col) == abs(x - idx):
                    break
            else:
                dfs(x + 1)

    dfs(0)
    return answer
