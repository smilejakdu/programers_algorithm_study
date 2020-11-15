'''
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.


s	    return
abcde	c
qwer	we
'''


s = 'qwer'

def solution(s):
    if len(s) % 2 == 0:
        return s[len(s)//2-1]+s[len(s)//2]
    else:
        return s[len(s)//2]


print(solution(s))

# 다른사람 풀이
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]

print(string_middle("qwer"))

