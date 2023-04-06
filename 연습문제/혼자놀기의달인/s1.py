def solution(cards):
    arr = []
    cnt_arr = [0]

    for i in range(len(cards)):
        target = i + 1
        card = cards[i]

        if card in arr:
            continue

        arr.append(card)
        cnt = 1
        while card != target:
            arr.append(cards[card - 1])
            card = cards[card - 1]
            cnt += 1

        cnt_arr.append(cnt)

        if len(arr) == len(cards):
            break

    cnt_arr.sort(reverse=True)

    return cnt_arr[0] * cnt_arr[1]
