import sys
sys.stdin = open('input.txt', encoding='UTF8')

target = input()
arr = []
num = 0

for i in range(len(target)):
    if '0' <= target[i] <= '9':
        num += int(target[i])
    else:
        arr.append(target[i])

arr.sort()
result = ''.join(arr) + str(num)
print(result)
