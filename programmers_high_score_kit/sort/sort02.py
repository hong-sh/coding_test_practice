'''
https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
'''

from itertools import permutations
def solution3(numbers):
    answer = '0'
    permutation = permutations(range(len(numbers)), len(numbers))
    for pm in permutation:
        tmp_str = ""
        for idx in pm:
            tmp_str += str(numbers[idx])
        answer = max(int(answer), int(tmp_str))
    return str(answer)


def solution2(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = list(str(numbers[i]))
    numbers.sort(reverse=True)
    for number in numbers:
        answer += number

    return answer

    
from itertools import permutations
def solution1(numbers):
    answer = '0'
    len_num = len(numbers)
    str_numbers = []
    permutation = permutations(range(len_num), len_num)
    for pm in permutation:
        tmp_str = ""
        for idx in pm:
            tmp_str += str(numbers[idx])

        str_numbers.append(tmp_str)
    answer = sorted(str_numbers, reverse=True)[0]

    return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

if __name__ == "__main__":
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))
