'''
https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5
'''

def solution(priorities, location):
    answer = 1
    q = []
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    ordered_priorities = sorted(priorities, reverse=True)
    priority_idx = 0
    while q:
        current_priority, idx = q.pop(0)
        max_priority = ordered_priorities[priority_idx]
        if idx == location and max_priority <= current_priority:
            return answer

        if max_priority <= current_priority:
            priority_idx += 1
            answer += 1
        else:
            q.append((current_priority, idx))

    return answer

def solution2(priorities, location):
    answer = 1
    ordered_priorities = sorted(priorities, reverse=True)
    printed = [False] * len(priorities)
    priority_idx = 0
    idx = 0
    while True:
        if printed[idx] is True:
            continue

        current_priority = priorities[idx]
        max_priority = ordered_priorities[priority_idx]
        if idx == location and max_priority <= current_priority:
            return answer

        if max_priority <= current_priority:
            priority_idx += 1
            answer += 1
            printed[idx] = True

        idx = (idx + 1) % len(priorities)

    return answer

if __name__ == "__main__":
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))