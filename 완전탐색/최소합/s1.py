import sys
import heapq
sys.stdin = open('input.txt', encoding='UTF8')

d = [(1, 0), (0, 1)]

for num in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    heap = []
    heapq.heappush(heap, (board[0][0], 0, 0))
    result = board[0][0]

    while heap:
        value, x, y = heapq.heappop(heap)
        if x == n - 1 and y == n - 1:
            result = value
            break

        for i in range(2):
            nx, ny = x + d[i][0], y + d[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                heapq.heappush(heap, (value + board[nx][ny], nx, ny))

    print('#{} {}'.format(num, result))
