'''
https://programmers.co.kr/learn/courses/30/lessons/42862
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
'''


def solution(n, lost, reserve):
    answer = 0
    
    state = [1] * n
    for i in range(len(lost)):
        state[lost[i]-1] -= 1
    
    for i in range(len(reserve)):
        state[reserve[i]-1] += 1
        
    if state[0] == 0 and state[1] == 2:
        state[0], state[1] = 1, 1
        
    if state[n-1] == 0 and state[n-2] == 2:
        state[n-1], state[n-2] = 1, 1
        
    for i in range(1, len(state)-1):
        if state[i] == 0 and state[i-1] == 2:
            state[i], state[i-1] = 1, 1
        if state[i] == 0 and state[i+1] == 2:
            state[i], state[i+1] = 1, 1
            
    for i in range(len(state)):
        if state[i] >= 1:
            answer += 1
            
    return answer