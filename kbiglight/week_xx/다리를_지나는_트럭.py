from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    l = len(trucks)
    bridge = deque([0 for _ in range(bridge_length)])
    passed_trucks = deque()
    total_weight = 0
    
    print(trucks, bridge, passed_trucks, total_weight)
    while True:
    # for _ in range(4):
        # if no more trucks to move and bridge is empty
        if len(passed_trucks) == l:
            break
        
        # move trucks which are on the bridge
        item = bridge.popleft()
        # if truck has crossed the bridge,
        # decrease total weight and add to passed truck list
        if item != 0:
            print(item, answer)
            total_weight -= item
            passed_trucks.append(item)
        bridge.append(0)
        
        
        if bridge and not trucks:
            # do nothing 
            pass
        elif total_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.pop()
            bridge.append(truck)
            total_weight += truck
        else :
            # do nothing only add one more second
            pass
        # print(trucks, bridge, passed_trucks, total_weight)
        
        answer += 1
        
    return answer