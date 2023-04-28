import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
result = 0

for i in range(1, len(blocks) - 1):
    max_left = max(blocks[:i])
    max_right = max(blocks[i+1:])

    if max_left > blocks[i] and max_right > blocks[i]:
        result += min(max_left, max_right) - blocks[i]

print(result)

