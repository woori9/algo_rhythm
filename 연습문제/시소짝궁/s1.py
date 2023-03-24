def solution(weights):
    dp = [0] * 1001
    result = 0
    weights.sort()

    for i in range(len(weights)):
        weight = weights[i]

        for num in [1, 1 / 2, 2 / 3, 3 / 4]:
            idx = int(weight * num)
            if weight * num == idx:
                result += dp[idx]

        dp[weight] += 1
    return result
