from itertools import permutations


def solution(n, weak, dist):
    INF = 1e9
    m = len(weak)
    weak += [weak[i] + n for i in range(len(weak) - 1)]
    answer = INF

    for i in range(m):
        for element in permutations(dist, len(dist)):
            stack = weak[i: i + m]

            for j in range(len(element)):
                target = stack.pop() - element[j]

                while stack and stack[-1] >= target:
                    stack.pop()

                if not stack:
                    if answer > j + 1:
                        answer = j + 1
                    break

    if answer == INF:
        answer = -1
    return answer
