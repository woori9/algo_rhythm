import sys
sys.stdin = open('input.txt', encoding='UTF8')


def move(cnt, battery, station):
    global result

    if cnt >= result:
        return

    for distance in range(battery, 0, -1):
        next_station = station + distance

        if next_station >= n:
            result = cnt
            return

        move(cnt + 1, stations[next_station], next_station)


for case in range(1, int(input()) + 1):
    stations = list(map(int, input().split()))
    n = stations[0]
    result = n

    move(0, stations[1], 1)

    print('#{} {}'.format(case, result))



