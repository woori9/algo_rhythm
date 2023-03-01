def solution(n):
    dp = [0] * (n + 1)
    dp[2] = 3

    for i in range(4, n + 1, 2):
        m = i - 4
        val = 0
        while m:
            val += dp[m] * 2
            m -= 2

        dp[i] = (dp[i - 2] * 3 + val + 2) % 1000000007

    return dp[n]
