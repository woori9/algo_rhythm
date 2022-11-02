def solution(s):
    if len(s) == 1:
        return 1

    answer = len(s)

    for unit in range(1, len(s) // 2 + 1):
        result = ''
        cnt = 1
        for i in range(unit, len(s), unit):
            current = s[i: i + unit]
            if s[i - unit: i] == s[i: i + unit]:
                cnt += 1
            else:
                temp = str(cnt) + s[i - unit: i] if cnt > 1 else s[i - unit: i]
                result += temp
                cnt = 1

        temp = str(cnt) + current if cnt > 1 else current
        result += temp

        if answer > len(result):
            answer = len(result)
    return answer

