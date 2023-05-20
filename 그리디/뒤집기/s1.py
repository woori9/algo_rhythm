import sys
sys.stdin = open('input.txt', encoding='UTF8')

target = input()
group_zero = group_one = 0
current = target[0]

for i in range(1, len(target)):
    if current != target[i]:
        if current == '0':
            group_zero += 1
        else:
            group_one += 1

        current = target[i]

if current == '0':
    group_zero += 1
else:
    group_one += 1

print(min(group_zero, group_one))
