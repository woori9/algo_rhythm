def solution(input_string):
    cnt = [0] * 26
    answer = ''
    idx = ord(input_string[0]) - 97
    cnt[idx] = 1

    for i in range(1, len(input_string)):
        if input_string[i] != input_string[i - 1]:
            idx = ord(input_string[i]) - 97
            cnt[idx] += 1

    for i in range(len(cnt)):
        if cnt[i] > 1:
            answer += chr(i + 97)

    return answer or 'N'
