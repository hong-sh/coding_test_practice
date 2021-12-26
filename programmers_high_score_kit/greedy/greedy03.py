'''
https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
'''

def solution2(number, k):
    answer = ''
    while k > 0:
        new_numbers = []
        for i in range(len(number)):
            new_numbers.append(int(number[:i] + number[i+1:]))
        number = str(max(new_numbers))
        k -= 1
    answer = number
    return answer

def solution(number, k):
    answer = ''
    remain = len(number) - k
    max_idx = 0
    while remain > 0:
        for i in range(max_idx, len(number) - (remain - 1)):
            if int(number[max_idx]) < int(number[i]):
                max_idx = i
        answer += number[max_idx]
        max_idx += 1
        remain -= 1

    return answer

if __name__ == "__main__":
    number = "4177252841"
    k = 2
    print(solution(number, k))