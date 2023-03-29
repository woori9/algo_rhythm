def solution(scores):
    wonho_a, wonho_b = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    result = 1
    current_max_b = scores[0][1]

    for i in range(0, len(scores)):
        a, b = scores[i]

        if wonho_a < a and wonho_b < b:
            return -1

        if current_max_b > b:
            continue

        if a + b > wonho_a + wonho_b:
            result += 1
        current_max_b = b

    return result

