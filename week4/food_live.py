'''
https://programmers.co.kr/learn/courses/30/lessons/42891

food_times	k	result
[3, 1, 2]	5	1
'''
from queue import PriorityQueue

def solution(food_times, k):
    answer = 0
    for i in range(len(food_times)):
        food_times[i] = [food_times[i], i+1]
    
    food_times.sort(key=lambda x: x[0])
    food_len = len(food_times)

    food_idx = 0
    pre_sec = 0
    sec = food_times[food_idx][0] * (food_len - food_idx)
    while sec <= k:
        food_idx += 1
        if food_idx == food_len:
            return -1
        pre_sec = sec
        sec += (food_times[food_idx][0] - food_times[food_idx-1][0]) * (food_len - food_idx)

    sub_food_times = sorted(food_times[food_idx:], key=lambda x: x[1])
    time_idx = (k-pre_sec) % (food_len - food_idx)
    answer = sub_food_times[time_idx][1]

    return answer

if __name__ == "__main__":
    food_times = [3, 1, 2]
    food_times = [4, 2, 3, 7]
    k = 5

    print(solution(food_times, k))