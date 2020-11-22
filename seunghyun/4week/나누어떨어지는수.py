'''
arr	            divisor	        return
[5, 9, 7, 10]	5	            [5, 10]
[2, 36, 1, 3]	1	            [1, 2, 3, 36]
[3,2,6]	        10	            [-1]
'''
arr     = [5, 9, 7, 10]
divisor = 5

def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]

    if len(answer)==0:
        answer.append(-1)
        return answer

    answer.sort() # print( 하게되면 None 이 찍히게 됨 ) 
    # return 을 해줄려면 sorted(answer)
    return answer

print(solution(arr , divisor))

# 다른 사람 풀이

def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0];
    arr.sort()

    return arr if len(arr) != 0 else [-1]

# 삼항연산자 
# result = condition ? when True : when False;

'''
만약에 len(arr) 길이가 0 이 아니라면 참
아니라면 [-1] 로해서 -1 추가해서 return 하게 된다
'''
