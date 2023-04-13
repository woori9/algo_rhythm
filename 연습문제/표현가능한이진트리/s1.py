import math


# 부모가 0이면 자식도 0이면 성립. 부모가 0인데 자식이 1이면 성립하지 않는다.
def dfs(node, diff, binary_number):
    if diff == 0:
        return 1

    left_child = node - diff
    right_child = node + diff

    if binary_number[node - 1] == '0':
        if binary_number[left_child - 1] == '1':
            return 0

        if binary_number[right_child - 1] == '1':
            return 0

    if not dfs(left_child, diff // 2, binary_number):
        return 0

    if not dfs(right_child, diff // 2, binary_number):
        return 0

    return 1


def solution(numbers):
    answer = [0] * len(numbers)

    for i in range(len(numbers)):
        num_binary = bin(numbers[i])[2:]
        level = math.ceil(math.log2(len(num_binary) + 1))
        full_length = 2 ** level - 1
        full_binary = (full_length - len(num_binary)) * '0' + num_binary
        root = (2 ** level) // 2
        answer[i] = dfs(root, root // 2, full_binary)

    return answer

