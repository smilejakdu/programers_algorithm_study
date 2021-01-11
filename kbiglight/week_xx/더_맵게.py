from queue import PriorityQueue
import heapq
from collections import deque

def solution(scoville, K):
    answer = 0
    
#     # solution using deque
#     scoville = deque(sorted(scoville))
#     flag = False
#     while True:
#         easiest = scoville.popleft()
#         easier = scoville.popleft() 
#         answer += 1
#         scoville.append(easiest + easier * 2)
#         scoville = deque(sorted(scoville))
#         # print(scoville)
#         if scoville[0] > K:
#             flag = True
#             break
#         if len(scoville) == 1 and scoville[0] < K:
#             return -1
            
#         # 결론.
#         # 정확성만 생각하면 푸는 것은 가능하지만 절대로 효율성을 못 뚫는다.
        
    #solution using priority queue(heapq)
    heapq.heapify(scoville)
    while scoville:
        try:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
        except IndexError:
            return -1
        heapq.heappush(scoville, first + second*2)
        answer += 1
        if scoville[0] >= K:
            return answer
    return answer