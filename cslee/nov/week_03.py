def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        re_a = array[i - 1:j]
        result = sorted(re_a)[k - 1]
        answer.append(result)

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


def solution(s):
    s_len = len(s)
    if s_len % 2 == 0:
        p = s_len // 2
        answer = s[p-1:p + 1]
    else:
        p = s_len // 2
        answer = s[p]
    return answer


print(solution("week"))
