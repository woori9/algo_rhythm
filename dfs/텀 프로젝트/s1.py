import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    group = [0] * (n + 1)
    visited = [0] * (n + 1)
    result = 0

    def make_group(idx_student):
        pick_student = students[idx_student]

        if visited[pick_student]:
            return pick_student

        else:
            visited[idx_student] = 1
            target = make_group(pick_student)

            if target == idx_student:
                current = idx_student
                group[current] = 1
                while students[current] != target:
                    current = students[current]
                    group[current] = 1

            return target

    for i in range(1, n + 1):
        if not visited[i]:
            make_group(i)

    print(group.count(0) - 1)

