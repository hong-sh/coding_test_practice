'''
https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

clothes	return
[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	3
'''

def solution(clothes):
    answer = 0
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] not in clothes_dict:
            clothes_dict[cloth[1]] = [cloth[0]]
        else:
            clothes_dict[cloth[1]].append(cloth[0])

    combination = 1
    for key, value in clothes_dict.items():
        combination *= len(value) + 1
    answer = combination - 1

    
    return answer


if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))