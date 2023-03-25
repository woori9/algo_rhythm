def calculate_cost(pick, mineral):
    graph = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    dict_mineral = {
        'diamond': 0,
        'iron': 1,
        'stone': 2
    }
    return graph[pick][dict_mineral.get(mineral)]


def solution(picks, minerals):
    result = float('inf')

    def dfs(cost, idx):
        nonlocal result

        if cost >= result:
            return

        if idx >= len(minerals) or sum(picks) == 0:
            result = cost
            return

        for i in range(len(picks)):
            next_cost = cost

            if picks[i] > 0:
                picks[i] -= 1
                for j in range(idx, idx + 5):
                    if j >= len(minerals):
                        break
                    next_cost += calculate_cost(i, minerals[j])
                dfs(next_cost, idx + 5)
                picks[i] += 1

    dfs(0, 0)
    return result
