import heapq


def solution(food_times, k):
    heap = [(item, idx + 1) for idx, item in enumerate(food_times)]
    heapq.heapify(heap)
    last_food_time = 0

    while heap:
        time = heap[0][0] - last_food_time

        if k - time * len(heap) < 0:
            break

        k -= time * len(heap)
        food = heapq.heappop(heap)
        last_food_time = food[0]

    if not heap:
        return -1

    idx = k % len(heap)
    heap.sort(key=lambda x: x[1])
    return heap[idx][1]
