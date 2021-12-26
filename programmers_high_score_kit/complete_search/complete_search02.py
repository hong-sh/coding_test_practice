'''
https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
numbers	return
"17"	3
"011"	2
'''

from itertools import permutations
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    primes = []
    for i in range(1, len(numbers)+1):
        pm = permutations(range(len(numbers)), i)
        for p in pm:
            num = ""
            for i in p:
                num += numbers[i]
            num = int(num)
            if num >= 2 and is_prime(int(num)):
                primes.append(int(num))
                
    answer = len(set(primes))
    return answer