'''
n    weak                dist            result
12    [1, 5, 6, 10]       [1, 2, 3, 4]    2
12    [1, 3, 4, 9, 10]    [3, 5, 7]       1

N = 200
weak = [0, 100]
dist = [1,1]

answer = 2

n = 200
weak[] = [0, 10, 50, 80, 120, 160]
dist[] = [1, 10, 5, 40, 30]
return = 3
'''
from itertools import permutations

def solution(n, weak, dist):
    weak_length = len(weak)
    for i in range(weak_length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    for i in range(weak_length):
        
        start_point = [weak[j] for j in range(i, i + weak_length)]
        
        candidates = permutations(dist, len(dist))
        
        for order in candidates:
            friend_idx, friend_count = 0, 1
            possible_check_length = start_point[0] + order[friend_idx]
            
            for idx in range(weak_length):
                if start_point[idx] > possible_check_length:
                    friend_count += 1
                    if friend_count > len(order):
                        break
                    friend_idx += 1
                    possible_check_length = order[friend_idx] + start_point[idx]
            answer = min(answer, friend_count)
    
    if answer > len(dist):
        return -1
    
    return answer 


if __name__ == "__main__":
    n = 200
    weak = [0, 10, 50, 80, 120, 160]
    dist = [1, 10, 5, 40, 30]
    print(solution(n, weak, dist))