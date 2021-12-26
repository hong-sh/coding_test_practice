'''
https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
'''

templete = {
    1 : [1, 2, 3, 4, 5],
    2 : [2, 1, 2, 3, 2, 4, 2, 5],
    3 : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
}

def solution(answers):
    answer = []
    max_score = 0
    for key, value in templete.items():
        score = 0
        for i in range(len(answers)):
            if answers[i] == value[i % len(value)]:
                score += 1
        if max_score < score:
            answer = [key]
            max_score = score
        elif max_score == score:
            answer.append(key)
    return answer