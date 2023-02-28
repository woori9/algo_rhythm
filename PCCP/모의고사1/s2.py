def solution(ability):
    category = len(ability[0])
    visited = [0] * len(ability)
    answer = 0

    def dfs(category_idx, score):
        nonlocal answer

        if category_idx == category:
            if score > answer:
                answer = score
            return

        for i in range(len(ability)):
            if not visited[i]:
                visited[i] = 1
                dfs(category_idx + 1, score + ability[i][category_idx])
                visited[i] = 0

    dfs(0, 0)
    return answer
