import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

m = int(input())
s = set()
all_arr = [i for i in range(1, 21)]

for _ in range(m):
    target = input().split()

    if len(target) == 1:
        if target[0] == 'empty':
            s = set()
        elif target[0] == 'all':
            s = set(all_arr)

    else:
        cmd, number = target
        number = int(number)

        if cmd == 'add':
            s.add(number)

        elif cmd == 'remove':
            s.discard(number)

        elif cmd == 'check':
            if number in s:
                print(1)
            else:
                print(0)

        elif cmd == 'toggle':
            if number in s:
                s.remove(number)
            else:
                s.add(number)
