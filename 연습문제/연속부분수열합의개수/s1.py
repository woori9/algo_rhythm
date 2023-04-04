def solution(elements):
    n = len(elements)
    results = set()
    sum_elements = [0] * n
    idx_after = 0

    for _ in range(n):
        for i in range(n):
            idx = (i + idx_after) % n
            sum_elements[i] += elements[idx]
        results.update(sum_elements)
        idx_after += 1

    return len(results)

