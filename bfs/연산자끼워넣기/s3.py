import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

dict_calc = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y, z = 1: (x * z) // y * z
}

n = int(input())
numbers = list(map(int, input().split()))
a, b, c, d = list(map(int, input().split()))
min_val = 1e9
max_val = -1e9


def dfs(idx, num):
    global min_val, max_val, a, b, c, d

    if idx == n:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
        return

    if a > 0:
        a -= 1
        dfs(idx + 1, dict_calc.get('+')(num, numbers[idx]))
        a += 1

    if b > 0:
        b -= 1
        dfs(idx + 1, dict_calc.get('-')(num, numbers[idx]))
        b += 1

    if c > 0:
        c -= 1
        dfs(idx + 1, dict_calc.get('*')(num, numbers[idx]))
        c += 1

    if d > 0:
        d -= 1

        if num < 0:
            dfs(idx + 1, dict_calc.get('/')(num, numbers[idx], -1))
        else:
            dfs(idx + 1, dict_calc.get('/')(num, numbers[idx]))

        d += 1


dfs(1, numbers[0])

print(max_val)
print(min_val)

