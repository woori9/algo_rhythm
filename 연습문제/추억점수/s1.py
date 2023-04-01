def solution(name, yearning, photo):
    answer = [0] * len(photo)
    dict_yearning = {}
    for i in range(len(name)):
        dict_yearning[name[i]] = yearning[i]

    for i in range(len(photo)):
        score = 0
        for j in range(len(photo[i])):
            score += dict_yearning.get(photo[i][j], 0)

        answer[i] = score
    return answer

