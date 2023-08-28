from itertools import combinations_with_replacement


def solution(k, n, reqs):
    answer = 1e9

    mentoring = [i for i in range(1, k + 1)]
    for element in combinations_with_replacement(mentoring, n - k):
        total_wait_time = 0
        cnt_mentors = [1] * (k + 1)
        for mentor in element:
            cnt_mentors[mentor] += 1

        mentors = [[0] * cnt_mentors[i] for i in range(len(cnt_mentors))]

        for i in range(len(reqs)):
            if total_wait_time > answer:
                break

            a, b, c = reqs[i]

            wait_time = 1e9
            idx = 0

            for j in range(len(mentors[c])):  # 끝나는 시간 저장
                if mentors[c][j] == 0:
                    mentors[c][j] = a + b
                    break

                if mentors[c][j] - a < wait_time:
                    wait_time = mentors[c][j] - a
                    idx = j
            else:
                if wait_time <= 0:
                    mentors[c][idx] = a + b
                else:
                    mentors[c][idx] += b
                    total_wait_time += wait_time

        if answer > total_wait_time:
            answer = total_wait_time

    return answer
