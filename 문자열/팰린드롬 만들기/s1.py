import sys
sys.stdin = open('input.txt', encoding='UTF8')

target = input()
cnt = [0] * 26

for i in range(len(target)):
    cnt[ord(target[i]) - 65] += 1

left = right = ''
middle = ''
result = ''

for i in range(len(cnt)):
    while cnt[i] > 1:
        left += chr(i + 65)
        right = chr(i + 65) + right
        cnt[i] -= 2

    if cnt[i] == 1:
        if middle:
            result = 'I\'m Sorry Hansoo'
            break

        middle = chr(i + 65)

print(result or left + middle + right)
