import heapq


def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)

    result = len(enemy)
    heap = []
    current_n = n

    for i in range(len(enemy)):
        if current_n >= enemy[i]:
            heapq.heappush(heap, (-enemy[i]))
            current_n -= enemy[i]
            continue

        if k == 0:
            result = i
            break

        heapq.heappush(heap, (-enemy[i]))
        current_n -= enemy[i]
        largest_enemy = heapq.heappop(heap)
        current_n += (largest_enemy * -1)
        k -= 1

    return result
