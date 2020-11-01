def solution(numbers):

    answer = []

    answer = [numbers[number1] + numbers[number2]) for number1 in range(0, len(numbers)) for number2 in
     range(number1, len(numbers)) if number1 != number2 and numbers[number1] + numbers[number2] not in answer]

    return sorted(answer)
