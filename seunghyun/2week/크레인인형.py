def solution(board, moves):

    answer = 0
    bucet  = []

    for move in moves:

        for j in range(len(board)):

            if board[j][move - 1] != 0:
                bucet.append(board[j][move - 1])
                board[j][move - 1] = 0

                if len(bucet) > 1:
                    if bucet[-1] == bucet[-2]:
                        bucet.pop(-1)
                        bucet.pop(-1)
                        answer += 2
                break

    return answer
