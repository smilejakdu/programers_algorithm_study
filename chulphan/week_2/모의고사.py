def solution(answers):
    # 1번 수포자가 찍는 방식
    ps1 = [1, 2, 3, 4, 5]
    # 2번 수포자가 찍는 방식
    ps2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # 3번 수포자가 찍는 방식
    ps3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score1 = 0
    score2 = 0
    score3 = 0

    for i, v in enumerate(answers):
        # 각각 현재 답에 뭐라고 찍었는지
        pattern1 = i % len(ps1)
        pattern2 = i % len(ps2)
        pattern3 = i % len(ps3)

        # 맞췄으면 점수 + 1
        if v == ps1[pattern1]:
            score1 += 1
        if v == ps2[pattern2]:
            score2 += 1
        if v == ps3[pattern3]:
            score3 += 1

    # 3명 중 가장 큰 점수 계산
    # maxScore = max(score1, max(score2, score3))
    maxScore = max(score1, score2, score3)

    result = []

    if score1 == maxScore:
        result.append(1)
    if score2 == maxScore:
        result.append(2)
    if score3 == maxScore:
        result.append(3)

    return result
