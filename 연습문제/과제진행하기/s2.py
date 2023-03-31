def solution(plans):
    answer = []
    for i in range(len(plans)):
        subject, starttime, playtime = plans[i]
        h, m = map(int, starttime.split(':'))
        print(h, m)
        plans[i][1] = h * 60 + m
        plans[i][2] = int(playtime)
    plans.sort(key=lambda x: x[1])
    stack = [[plans[0][0], plans[0][2]]]  # 마지막 요소가 진행 중 과목 이름, playtime

    for i in range(1, len(plans)):
        subject, starttime, playtime = plans[i]
        time_difference = starttime - plans[i - 1][1]

        while time_difference and stack:
            subject_ing, playtime_ing = stack[-1]

            if playtime_ing > time_difference:
                stack[-1][1] = playtime_ing - time_difference
                break

            answer.append(subject_ing)
            time_difference -= playtime_ing
            stack.pop()

        stack.append([subject, playtime])

    while stack:
        element = stack.pop()
        answer.append(element[0])

    return answer
