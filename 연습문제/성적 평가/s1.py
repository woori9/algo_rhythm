import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

n = int(input())
score = [list(map(lambda x: (int(x[1]), x[0]), enumerate(input().split()))) for _ in range(3)]
sum_score = [[0, i] for i in range(n)]

for i in range(len(score)):
    score[i].sort(reverse=True)
    result = [0] * n
    rank = temp_rank = 1
    standard_score = 1000

    for j in range(n):
        value, idx = score[i][j]
        sum_score[idx][0] += value

        if value < standard_score:
            rank = temp_rank
            standard_score = value

        result[idx] = rank
        temp_rank += 1
    print(*result)

result = [0] * n
rank = temp_rank = 1
standard_score = 3000
sum_score.sort(reverse=True)

for i in range(len(sum_score)):
    value, idx = sum_score[i]

    if value < standard_score:
        rank = temp_rank
        standard_score = value

    result[idx] = rank
    temp_rank += 1
print(*result)
