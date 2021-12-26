'''
https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3
brown	yellow	return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
'''

import math
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3, int(math.sqrt(total)) + 1):
        if total % i != 0:
            continue 
            
        if (i - 2) * ((total // i) - 2) == yellow:
            answer = [(total // i), i]
    return answer