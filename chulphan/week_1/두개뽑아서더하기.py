def solution(numbers):
    result = []
    for idx, value in enumerate(numbers):
        for j in numbers[idx + 1:]:
            sum = value + j
            if sum not in result:
                result.append(sum)
    result = sorted(result)
    return result