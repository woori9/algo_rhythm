def deliver_or_pickup(cap, target_list):
    idx = 0
    current = cap
    while target_list and current:
        if not target_list[-1]:
            target_list.pop()
            continue

        if not idx:
            idx = len(target_list)

        if target_list[-1] > current:
            target_list[-1] -= current
            current = 0
        else:
            cnt = target_list.pop()
            current -= cnt
    return idx


def solution(cap, n, deliveries, pickups):
    answer = 0

    while deliveries or pickups:
        d_idx = deliver_or_pickup(cap, deliveries)
        p_idx = deliver_or_pickup(cap, pickups)
        answer += 2 * max(d_idx, p_idx)

    return answer
