'''
n	info	result
5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]

'''

from itertools import combinations

def solution(n, info):
    answer = []

    comb_list = list(combinations(range(10* n), n))

    for comb in comb_list:
        score_list = [0] * 10
        for c in comb:
            score_list[c % 10] += 1
        
        ryan, apeach = 0, 0
        max_ryan = -1
        for i in range(len(score_list)):
            if score_list[i] == 0 and info[i] == 0:
                continue

            if score_list[i] > info[i]:
                ryan += 10 - i
            else:
                apeach += 10 - i
            
        if ryan > apeach and max_ryan >= ryan:
            answer = score_list

    return answer


if __name__ == "__main__":
    n = 5
    info = [2,1,1,1,0,0,0,0,0,0,0]
    print(solution(n, info))