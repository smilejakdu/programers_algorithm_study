# 콜라츠 추측 , 소수 찾기 입니다!
#
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
#
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)
#
# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.
# 입출력 예
# n	result
# 10	4
# 5	3
# 입출력 예 설명
# 입출력 예 #1
# 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환
# 1부터 10 사이의 소수는 2,3,5,7  1과 자신만으로 나눠지는것.
# 입출력 예 #2
# 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환

# 효율성 실패
# def solution(n):
#     answer = 0
#     for num in range(2, n + 1):
#         print(f"num:{num}", end="\n")
#         count = 0
#         print("====prime number search====")
#         for n in range(2, num + 1):
#             print(f"{num}%{n}={num % n}")
#             if num % n == 0:
#                 count += 1
#             if count > 1:
#                 break
#         if count == 1:
#             answer += 1
#         print(f"answer:{answer}")
#     return answer

def valid_prime_number(num):
    if num == 2:
        return True
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def solution(n):
    answer = 0
    for num in range(2, n + 1):
        if valid_prime_number(num):
            answer += 1
    return answer


print(solution(10))