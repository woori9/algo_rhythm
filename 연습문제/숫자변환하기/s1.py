from collections import deque


def solution(x, y, n):
    if x == y:
        return 0

    answer = -1
    visited = {x}
    queue = deque([(x, 0)])

    while queue:
        number, cnt = queue.popleft()

        a, b, c = number + n, number * 2, number * 3

        for num in [a, b, c]:
            if num > y:
                continue

            if num == y:
                answer = cnt + 1
                queue.clear()
                break

            prev = len(visited)
            visited.add(num)

            if len(visited) > prev:
                queue.append((num, cnt + 1))

    return answer
