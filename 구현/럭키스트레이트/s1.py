import sys
sys.stdin = open('input.txt', encoding='UTF8')

x = int(input())
numbers = []

while x > 0:
    q, r = x // 10, x % 10
    x = q
    numbers.append(r)

length = len(numbers) // 2
n1, n2 = numbers[: length], numbers[length:]

if sum(n1) == sum(n2):
    print('LUCKY')
else:
    print('READY')

