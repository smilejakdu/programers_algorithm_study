import collections


def solution(board, moves):
    preprocess = []
    result = []

    counts = 0

    # *board -> 주어진 2차원 배열 내 원소를 모두 꺼냄 -> [], [], ...
    for x in zip(*board):
        # 0 이 아닌 친구들만 큐에 넣어 새로운 배열에 넣어줌
        preprocess.append(collections.deque([i for i in x if i != 0]))

    for move in moves:
        # moves 내 원소를 인덱스 처리
        current_col = move - 1
        if len(preprocess[current_col]):
            # 해당하는 move 위치에 맨 위에 인형을 담는다
            result.append(preprocess[current_col].popleft())

    idx = 0
    while True:
        if idx >= len(result) - 1:
            break
        # 현재 인형과 이전에 담긴 인형이 같으면 없애주는 작업
        if result[idx] == result[idx + 1]:
            result.pop(idx)
            result.pop(idx)
            counts += 2
            idx = 0
        else:
            idx += 1

    return counts
