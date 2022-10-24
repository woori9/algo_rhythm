import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

from collections import deque
from copy import deepcopy

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
    q.append((numbers[0], 1, deepcopy(calc)))

queue = deque(q)

results = set([])

while queue:
    number, next_idx, cnt_operators = queue.popleft()
    if next_idx == n:
        results.add(number)
        continue

    for i in range(4):
        if cnt_operators[i]:
            operator = operators[i]
            copy = deepcopy(cnt_operators)

            if operator == '/' and number < 0:
                result = dict_calc.get(operators[i])(number, numbers[next_idx], -1)
            else:
                result = dict_calc.get(operators[i])(number, numbers[next_idx])
            copy[i] -= 1
            queue.append((result, next_idx + 1, copy))

print(max(results))
print(min(results))
