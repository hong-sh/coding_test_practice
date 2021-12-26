'''
https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3
citations	return
[3, 0, 6, 1, 5]	3
'''


def solution(citations):
    answer = 0
    citations.sort()
    num_citations = len(citations)
    for i in range(num_citations):
        if num_citations - i <= citations[i]:
            answer = num_citations - i
            break
            
    return answer


if __name__ == "__main__":
    citations = [3, 4, 5, 8, 25]
    print(solution(citations))