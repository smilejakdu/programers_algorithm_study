'''
answers         return
[1,2,3,4,5]     [1]
[1,3,2,4,2]     [1,2,3]

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
'''

answers = [2,4,1,3,5,5,1,2]

def solution(answers):

    supo_list    = [[1, 2, 3, 4, 5],
                    [2, 1, 2, 3, 2, 4, 2, 5],
                    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    answer_list  = [0 , 0 , 0]

    for index in range(0 , len(answers)):
        if supo_list[0][index % len(supo_list[0])] == answers[index]:
            answer_list[0] += 1

        if supo_list[1][index % len(supo_list[1])] == answers[index]:
            answer_list[1] += 1

        if supo_list[2][index % len(supo_list[2])] == answers[index]:
            answer_list[2] += 1

    max_number  = max(answer_list)
    result_list = []

    for index in range(0 , len(answer_list)):
        if max_number == answer_list[index]:
            result_list.append(index + 1)

    return result_list
