def solution(n, money):
    dp = [0] * (n + 1)
    money.sort()

    for price in money:
        dp[price] += 1

        for i in range(price + 1, n + 1):
            dp[i] += dp[i - price]

    return dp[n]
