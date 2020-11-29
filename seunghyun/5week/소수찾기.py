'''
n       result
10      4
5       3
'''

n = 10
def solution2(n):
    num = set(range(2 , n+1))
    print(num)

    for i in range(2 , n+1):
        if i in num:
            num-=set(range(2*i , n+1, i))
    return len(num)

print(solution2(n))
