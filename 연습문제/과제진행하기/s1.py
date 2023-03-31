def get_time_difference(prev_time, current_time):
    h1, m1 = prev_time  # 10:40 11:10
    h2, m2 = current_time  # 11:20 12:20 12:05
    h = h2 - h1
    m = 0

    if m2 >= m1:
        m = m2 - m1
    else:
        m = 60 + m2 - m1
        h -= 1

    return h * 60 + m


def solution(plans):
    answer = []
    for i in range(len(plans)):
        subject, starttime, playtime = plans[i]
        plans[i][1] = list(map(int, starttime.split(':')))
        plans[i][2] = int(playtime)
    plans.sort(key=lambda x: (x[1][0], x[1][1]))
    stack = [[plans[0][0], plans[0][2]]]  # 마지막 요소가 진행 중 과목 이름, playtime

    for i in range(1, len(plans)):
        subject, starttime, playtime = plans[i]
        time_difference = get_time_difference(plans[i - 1][1], starttime)

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

