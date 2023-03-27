import heapq


def solution(storey):
    answer = float('inf')
    queue = [(0, storey)]

    while queue:
        cost, current = heapq.heappop(queue)

        if current < 10:
            answer = min(answer, cost + current, cost + 10 - current + 1)
            continue

        q, r = current // 10, current % 10

        if q:
            heapq.heappush(queue, (cost + r, q))
        heapq.heappush(queue, (cost + (10 - r), q + 1))

    return answer

