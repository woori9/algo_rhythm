def solution(topping):
    answer = 0
    cnt_arr = [0] * (max(topping) + 1)

    for i in range(len(topping)):
        cnt_arr[topping[i]] += 1

    plate_a = set(topping)
    plate_b = set()
    idx = 0

    while idx < len(topping):
        plate_b.add(topping[idx])
        cnt_arr[topping[idx]] -= 1

        if cnt_arr[topping[idx]] == 0:
            plate_a.remove(topping[idx])

        if len(plate_a) == len(plate_b):
            answer += 1
        idx += 1

    return answer

