# 연속된 부분 수열의 합, 음수를 포함할 때


def solution(sequence):
    dp1 = [0] * len(sequence)
    dp2 = [0] * len(sequence)

    for i in range(0, len(sequence), 2):
        sequence[i] *= -1

    dp1[0] = sequence[0]

    for i in range(1, len(dp1)):
        dp1[i] = max(sequence[i], dp1[i - 1] + sequence[i])

    dp2[0] = sequence[0]
    for i in range(len(sequence)):
        sequence[i] *= -1
        dp2[i] = max(sequence[i], dp2[i - 1] + sequence[i])

    return max(dp1 + dp2)
