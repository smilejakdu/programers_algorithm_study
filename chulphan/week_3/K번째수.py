def solution(array, commands):
    answer = []

    for i in commands:
        c1, c2, c3 = i
        if c1 == c2:
            answer.append(array[c1-1])
        else:
            copied = array[c1-1:c2]
            copied.sort()
            answer.append(copied[c3-1])
    return answer
