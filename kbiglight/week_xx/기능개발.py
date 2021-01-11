from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    deploy = deque()
    queue = deque()
    
    for i in range(len(progresses)):
        require = 100 - progresses[i]
        time = math.ceil(require / speeds[i])
        deploy.append(time)
    print("deploy : " , deploy)
    
    
    while deploy:
        target = deploy.popleft()
        if not queue:
            queue.append(target)
            continue
        print("queue : ", queue)
        if target > queue[0]:
            answer.append(len(queue))
            queue.clear()
            queue.append(target)
        else :
            queue.append(target)
            
    # 만약 큐가 아직 비어있지 않다면
    # 큐에 있는 갯수도 넣어줘야 한다.
    if queue:
        answer.append(len(queue))

    return answer