'''

https://programmers.co.kr/learn/courses/30/lessons/72411

orders	course	result
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]
'''
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in range(len(orders)):
        orders[i] = ''.join(sorted(orders[i]))

    for c in course:
        combination_list = []
        for order in orders:
            combination_list.extend(combinations(order, c))
        combination_list = set(combination_list)
        order_cnt = []
        for combination in combination_list:
            cnt = 0
            for order in orders:
                is_in = True
                for comb in combination:
                    if comb not in order:
                        is_in = False
                        break

                cnt += 1 if is_in else 0

            if cnt >= 2:
                order_cnt.append([combination, cnt])
        
        if len(order_cnt) == 0:
            continue

        order_cnt.sort(key= lambda x : x[1], reverse=True)
        max_cnt = max(order_cnt, key= lambda x : x[1])
        for combination, cnt in order_cnt:
            if cnt == max_cnt[1]:
                answer.append(''.join(sorted(''.join(combination))))
            else:
                break

    answer.sort()
    return answer


if __name__ == "__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2, 3, 4]
    print(solution(orders, course))