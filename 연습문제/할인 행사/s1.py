def solution(want, number, discount):
    answer = 0
    n = len(want)
    cnt_want = [0] * (n + 1)
    dict_idx = {}

    for i in range(len(want)):
        dict_idx[want[i]] = i

    for i in range(10):
        idx = dict_idx.get(discount[i], n)
        cnt_want[idx] += 1

    if cnt_want[:n] == number:
        answer += 1

    for i in range(len(discount) - 10):
        a = dict_idx.get(discount[i], n)
        b = dict_idx.get(discount[i + 10], n)

        cnt_want[a] -= 1
        cnt_want[b] += 1

        if cnt_want[:n] == number:
            answer += 1

    return answer
