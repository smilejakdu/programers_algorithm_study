# 두개 더 뽑아서 더하기
def solution1(numbers):
    answer = []
    idx = 1
    for number in numbers:
        for j in range(idx, len(numbers)):
            sum_num = number + numbers[j]
            if sum_num not in answer:
                answer.append(sum_num)
        idx += 1

    answer = sorted(answer)
    return answer


# 효율성 통과 실패
# def solution2(participant, completion):
#     answer = ''
#     failed_player = None
#     for player in completion:
#         if player in completion:
#             completion_player = completion.index(player)
#             del completion[completion_player]
#         else:
#             failed_player = player
#             break
#     return failed_player

# 선수
def solution2(participant, completion):
    answer = ''
    sorted_participant = sorted(participant)
    sorted_completion = sorted(completion)

    for idx in range(0, len(sorted_participant)):
        player = sorted_participant.pop()
        if len(sorted_completion) == 0:
            answer = player
            break
        completion_player = sorted_completion.pop()
        if player != completion_player:
            answer = player
            break
    return answer
