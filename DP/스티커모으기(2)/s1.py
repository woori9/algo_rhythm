def solution(sticker):
    n = len(sticker)

    if n == 1 or n == 2 or n == 3:
        return max(sticker)

    dp = [0] * n
    dp[0] = sticker[0]
    dp[1] = max(sticker[0], sticker[1])
    dp[2] = max(dp[0] + sticker[2], dp[1])

    dp2 = [0] * n
    dp2[1] = sticker[1]
    dp2[2] = max(sticker[1], sticker[2])

    for i in range(3, n):
        if i < (n - 1):
            dp[i] = max(dp[i - 3] + sticker[i], dp[i - 2] + sticker[i], dp[i - 1])
        dp2[i] = max(dp2[i - 3] + sticker[i], dp2[i - 2] + sticker[i], dp2[i - 1])

    return max(dp + dp2)
