import collections


def solution(participant, completion):
    party_count = collections.Counter(participant)
    completion_count = collections.Counter(completion)

    party_count.subtract(completion_count)
    return party_count.most_common(1)[0][0]

# 처음에 접근하려고 했던 방법은 주어진 input들을 각각의 딕셔너리로 변환
# key => 선수이름, value => 나타난 빈도
#     for key, value in completion_dict.items():
#         if key in party_dict:
#             party_dict[key] -= value

#     for key, value in party_dict.items():
#         if value >= 1:
#             return key
