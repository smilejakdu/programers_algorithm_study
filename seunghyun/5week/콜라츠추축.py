'''
n           result
6           8
16          4
626331      -1
'''

n = 6

def solution(num):
    answer = 0

    while num !=1:

        if answer ==500:
            return -1

        if num %2 == 0:
            answer +=1
            num = num // 2

        elif num %2 == 1:
            answer +=1
            num = num*3 + 1

    return answer

print(solution(n))


# 다른 사람 풀이

def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))

