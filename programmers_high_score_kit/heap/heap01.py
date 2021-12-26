'''
https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
'''

import heapq

def solution(scoville, K):
    answer = 0
    q = []
    for scv in scoville:
        heapq.heappush(q,scv)
    
    cnt = 0
    while q:
        if len(q) == 1 and q[0] < K:
            return -1
        
        first = heapq.heappop(q)
        if first >= K:
            return cnt
        
        second = heapq.heappop(q)
        heapq.heappush(q, (first + (second * 2)))
        cnt += 1
                       
    return answer

if __name__ == "__main__":

    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))