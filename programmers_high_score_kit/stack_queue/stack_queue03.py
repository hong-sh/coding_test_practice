'''
https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]

bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110
'''

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    current_weights = 0
    while truck_weights:

        for i in range(len(bridge)):
            bridge[i][1] += 1

        truck = truck_weights[0]
        if current_weights + truck <= weight:
            current_weights += truck
            truck_weights.pop(0)
            bridge.append([truck, 1])
            answer += 1
        else:
            answer += 1

        if bridge[0][1] == bridge_length:
            tmp = bridge.pop(0)
            current_weights -= tmp[0]

    return answer + bridge_length


if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10]
    print(solution(bridge_length, weight, truck_weights))

