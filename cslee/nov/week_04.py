# 문제 조건을 하나 못봄. 문제를 꼼꼼히 전부 읽어서 조건을 잘 뺴오자
# def solution(n, lost, reserve):
#     lost_count = len(lost)
#     reserve_count = len(reserve)
#
#     # 여분있는 사람들이 잃어버린 사람보다 많다면
#     if reserve_count > lost_count:
#         # 모든 인원이 있다.
#         answer = n
#     else:
#         # 여분이 모자르다면 이미 존재하는 사람을 구한다.
#         have_gym_suit_student_count = n - lost_count
#         # 이미 존재하는 사람과 여분이 존재하는 사람을 더한다.
#         answer = have_gym_suit_student_count + reserve_count
#     return answer

def solution(n, lost, reserve):
    # 중복 번호 없고, 여벌옷있는 친구들 중 도난 당한 친구들은 셀프 챙기기
    filtered_lost = set(lost) - set(reserve)
    filtered_reserve = set(reserve) - set(lost)

    # 여벌옷 있는 사람 번호
    for reserve_student_number in filtered_reserve:
        # 혹시 내 앞번호 친구 도난 당했니?
        if reserve_student_number - 1 in filtered_lost:
            # 도난 당했어 빌려줘...
            filtered_lost.remove(reserve_student_number - 1)
        # 앞번호는 있구나 혹시 뒷번호 친구 도난 당했니?
        elif reserve_student_number + 1 in filtered_lost:
            # 도난 당했어 빌려줘...
            filtered_lost.remove(reserve_student_number + 1)

        # 도난 당한 사람이 더이상 없니?
        if not filtered_lost:
            break
    answer = n - len(filtered_lost)
    return answer


ex_n = 5
ex_lost = [1, 2, 3, 4]
ex_reserve = [1, 4, 5]
ex_result = 4
result = solution(ex_n, ex_lost, ex_reserve)

if result == ex_result:
    print("clear")
else:
    print("failed")
