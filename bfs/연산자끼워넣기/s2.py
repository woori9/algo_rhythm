import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
calc = list(map(int, input().split()))
q = []

dict_calc = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y, z = 1: (x * z) // y * z
}

operators = ['+', '-', '*', '/']

for _ in range(n):
    q.append((numbers[0], 1, calc[0], calc[1], calc[2], calc[3]))

queue = deque(q)

results = set([])

while queue:
    number, next_idx, a, b, c, d = queue.popleft()
    cnt_operators = [a, b, c, d]

    if next_idx == n:
        results.add(number)
        continue

    for i in range(4):
        if cnt_operators[i]:
            copy = cnt_operators[:]
            operator = operators[i]

            if operator == '/' and number < 0:
                result = dict_calc.get(operators[i])(number, numbers[next_idx], -1)
            else:
                result = dict_calc.get(operators[i])(number, numbers[next_idx])
            copy[i] -= 1
            queue.append((result, next_idx + 1, copy[0], copy[1], copy[2], copy[3]))

print(max(results))
print(min(results))
