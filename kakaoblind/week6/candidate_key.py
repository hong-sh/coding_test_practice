'''
https://programmers.co.kr/learn/courses/30/lessons/42890

relation	result
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	2

'''

from itertools import combinations

def solution(relation):
    answer = 0

    tuple_num = len(relation)
    attribute_num = len(relation[0]) 
    key_idx = list(range(attribute_num))
    candidate_idx_list = []

    for i in range(1, attribute_num+1):
        combs = combinations(key_idx, i)
        for comb in combs:
            check_list = []
            for k in range(tuple_num):
                tuple_str = ""
                for j in comb:
                    tuple_str += relation[k][j]
                check_list.append(tuple_str)

            if len(set(check_list)) == tuple_num:
                is_subset = False
                for candidate_idx in candidate_idx_list:
                    if candidate_idx.issubset(comb):
                        is_subset = True
                        break

                if is_subset is False:
                    candidate_idx_list.append(set(comb))

    answer = len(candidate_idx_list)
    return answer


if __name__ == "__main__":
    relation = \
        [["100","ryan","music","2"],
        ["200","apeach","math","2"],
        ["300","tube","computer","3"],
        ["400","con","computer","4"],
        ["500","muzi","music","3"],
        ["600","apeach","music","2"]]


    print(solution(relation))
