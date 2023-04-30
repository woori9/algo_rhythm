def solution(targets):
    answer = 1
    targets.sort(key=lambda x: (x[0], x[1]))
    current_e = targets[0][1]
    idx = 1

    while idx < len(targets):
        s, e = targets[idx]
        idx += 1

        if s < current_e:
            current_e = min(current_e, e)
            continue

        answer += 1
        current_e = e

    return answer
