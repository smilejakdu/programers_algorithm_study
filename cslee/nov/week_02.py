# 크레인 문제
# N*N 행렬이 존재한다, 바구니가 존재한다.
# N의 위치에 해당하는 인형을 바구니로 옴긴다.
# 바구니에 연속으로 동일한 인형이 담긴다면 두 친구는 사라진다.
# 바구니는 모든 인형이 들어갈 수 있다고 가정함
from builtins import enumerate


class BoardGame:
    def __init__(self, board):
        self.board = board
        self.bucket = []
        self.answer = 0

    def get_doll(self, line_num):
        selected_line_num = line_num - 1

        selected_line = self.board[selected_line_num]
        line_length = len(selected_line)

        for i in range(0, line_length):
            doll = selected_line.pop()
            if doll != 0:
                return doll
            if len(selected_line) == 0:
                break
        return 0

    def push_doll_bucket(self, doll):
        bucket_len = len(self.bucket)
        if bucket_len == 0:
            self.bucket.append(doll)
        else:
            last_idx = bucket_len - 1
            last_doll = self.bucket[last_idx]
            if last_doll == doll:
                self.bucket.pop()
                self.answer += 2
            else:
                self.bucket.append(doll)

    def play(self, moves):
        for move_command in moves:
            doll = self.get_doll(move_command)
            if doll != 0:
                self.push_doll_bucket(doll)


def solution1(board, moves):
    board_game_obj = BoardGame(board)
    board_game_obj.play(moves)
    return board_game_obj.answer


print(solution1([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                [1, 5, 3, 5, 1, 2, 1, 4]))
