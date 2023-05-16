def solution(sequence, k):
    answer = []
    start = end = 0
    current = sequence[0]

    while start < len(sequence) and end < len(sequence):
        if current <= k:
            if current == k:
                if not answer or (answer[1] - answer[0]) > end - start:
                    answer = [start, end]
            end += 1

            if end == len(sequence):
                break

            current += sequence[end]
        else:
            current -= sequence[start]
            start += 1

            if start > end:
                break

    return answer
