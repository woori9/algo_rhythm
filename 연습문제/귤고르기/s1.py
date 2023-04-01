def solution(k, tangerine):
    answer = 0
    dict_cnt_tangerine = {}

    for i in range(len(tangerine)):
        dict_cnt_tangerine[tangerine[i]] = dict_cnt_tangerine.get(tangerine[i], 0) + 1

    cnt = list(dict_cnt_tangerine.values())
    cnt.sort(reverse=True)

    for i in range(len(cnt)):
        k -= cnt[i]
        answer += 1

        if k <= 0:
            break

    return answer

