import heapq


def solution(numbers):
    answer = [-1] * len(numbers)
    heap = []

    for i in range(len(numbers)):
        heapq.heappush(heap, (numbers[i], i))
        while heap:
            number, idx = heap[0]
            if number >= numbers[i]:
                break

            heapq.heappop(heap)
            answer[idx] = numbers[i]

    return answer

