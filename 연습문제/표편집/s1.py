def solution(n, k, cmd):
    result = ['O'] * n
    arr = [[i - 1, i + 1] for i in range(n)]
    arr[n - 1][1] = -1
    stack = []
    now = k

    for i in range(len(cmd)):
        command = cmd[i].split()

        if command[0] == 'U':
            for _ in range(int(command[1])):
                now = arr[now][0]

        if command[0] == 'D':
            for _ in range(int(command[1])):
                now = arr[now][1]

        if command[0] == 'C':
            stack.append(now)
            prev, next_ = arr[now]

            if prev != -1:
                arr[prev][1] = next_

            if next_ != -1:
                arr[next_][0] = prev

            result[now] = 'X'

            if next_ == -1:
                now = prev

                if now == -1:
                    now = 0
            else:
                now = next_

        if command[0] == 'Z':
            idx = stack.pop()
            prev, next_ = arr[idx]

            if prev != -1:
                arr[prev][1] = idx

            if next_ != -1:
                arr[next_][0] = idx
                
            result[idx] = 'O'

    return ''.join(result)

