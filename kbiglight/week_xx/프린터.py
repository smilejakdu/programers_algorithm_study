from queue import PriorityQueue
from collections import deque

def solution(priorities, location):
    answer = 0
    order = [i for i in range(0, len(priorities))]
    
#   PriorityQueue 사용 - 불가능
#   heapq를 사용한다? 가능성은 있다.
    # printer = PriorityQueue()
    # print(priorities, order)
    # for i in range(len(priorities)):
    #     printer.put((-priorities[i], order[i]))
    # print(printer.queue)
    # while not printer.empty():
    # # while True:
    #     item = printer.get()
    #     answer += 1
    #     print(item, printer.queue)
    #     if item[1] == location:
    #         break

    
    # solution using deque
    # O(n^2)
    printer = deque(list(zip(priorities, order)))
    top_priority = max(printer, key=lambda x : x[0])[0]
    count = 1
    while printer:
        doc = printer.popleft()
        # print(printer, doc, top_priority)
        # if doc has top priority
        if doc[0] == top_priority:
            # reset top priority value and add 1 to result 
            answer += 1
            if doc[1] == location:
                break
            top_priority = max(printer, key=lambda x : x[0])[0]
        # if printer's queue has upper priority the doc's...
        # put it back in printer's queue
        else:
            printer.append(doc)
        count += 1
    
    print(count)
            
    return answer