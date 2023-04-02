def get_divisor(number):
    result = []
    for i in range(1, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            result.append(i)
            result.append(number // i)

    result.sort(reverse=True)
    return result


def solution(arrayA, arrayB):
    min_a = min(arrayA)
    min_b = min(arrayB)
    divisor_a = get_divisor(min_a)
    divisor_b = get_divisor(min_b)
    divisor_a.pop()  # 1 제거
    divisor_b.pop()
    gcd_a = gcd_b = 0

    for i in range(len(divisor_a)):
        if not gcd_a:
            for j in range(len(arrayA)):
                if arrayA[j] % divisor_a[i]:
                    break
            else:
                gcd_a = divisor_a[i]

    for i in range(len(divisor_b)):
        if not gcd_b:
            for j in range(len(arrayB)):
                if arrayB[j] % divisor_b[i]:
                    break
            else:
                gcd_b = divisor_b[i]

    result = [0]

    if gcd_b:
        for a in arrayA:
            if a % gcd_b == 0:
                break
        else:
            result.append(gcd_b)

    if gcd_a:
        for b in arrayB:
            if b % gcd_a == 0:
                break
        else:
            result.append(gcd_a)

    return max(result)
