import sys
sys.stdin = open('input.txt', encoding='UTF8')
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = 0


def dfs(idx, sum_value, cnt):
    global result

    if sum_value > s and idx < len(arr) and arr[idx] > 0:
        return

    if sum_value == s and cnt > 0:
        result += 1
        # 처음에 return 해서 오답.
        # return 하게 되면 만약 다음에 고를 숫자가 0이 되었을 때 카운트하지 못한다.

    for i in range(idx, len(arr)):
        dfs(i + 1, sum_value + arr[i], cnt + 1)


dfs(0, 0, 0)

print(result)
