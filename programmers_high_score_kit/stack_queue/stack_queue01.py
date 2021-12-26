'''
https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
'''
import math

def solution(progresses, speeds):
    answer = []
    prev_complete = 1
    
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        complete = math.ceil(remain / speeds[i])
        if prev_complete >= complete:
            answer[-1] += 1
        else:
            answer.append(1)
            prev_complete = complete
            
    return answer

if __name__ == "__main__":
    progresses = [93,30,55]
    speeds = [1, 30,5]
    print(solution(progresses, speeds))