
import sys
sys.stdin = open("samsung/sample_input.txt", "r")

from itertools import product

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    
def calculate(a, b, op):
    if op == 1:
        return a + b
    elif op == 2:
        return a - b
    elif op == 3:
        return a * b
    elif op == 4:
        return a // b if b != 0 else -1

def valid_using_operators(current_number, current_operator, W, M, cnt, dp):
    if cnt > M:
        return int(1e+15)

    if (current_number, current_operator, cnt) in dp:
        return dp[(current_number, current_operator, cnt)]
    
    minimum_cnt = int(1e+15)
    
    if current_operator != 0: # select number
        for number in numbers:
            if number == 0 and current_operator == 4: # non zero
                continue
            
            next_number = calculate(current_number, number, current_operator)
            if 0 <= next_number <= 999:
                len_number = len(str(number))
                if next_number == W:
                    minimum_cnt = min(minimum_cnt, cnt + len_number + 1)
                else:
                    minimum_cnt = min(minimum_cnt, valid_using_operators(next_number, 0, W, M, cnt + len_number, dp))
    
    if current_operator == 0:
        for operator in operators:
            minimum_cnt = min(minimum_cnt, valid_using_operators(current_number, operator, W, M, cnt + 1, dp))

    dp[(current_number, current_operator, cnt)] = minimum_cnt
    return minimum_cnt
        
    

for test_case in range(1, T + 1):
    N, O, M = map(int, input().split()) 
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    
    two_comb = list(product(numbers, repeat=2))
    three_comb = list(product(numbers, repeat=3))
    
    for a, b in two_comb:
        numbers.append(a*10 + b)
        
    for a, b, c in three_comb:
        number = 100*a + 10*b + c
        if number <= 999:
            numbers.append(number)
            
    numbers = list(set(numbers))
        
    W = int(input())
    
    minimum_number = int(1e+15)
    dp = {}
    
    if W == 0 and W in numbers:
        print(f"#{test_case} 1") 
        continue
    
    if W in numbers:
        minimum_number = min(minimum_number, len(str(W)))
        
    minimum_number = min(minimum_number, valid_using_operators(0, 1, W, M, 0, dp))
    print(f"#{test_case} {minimum_number if minimum_number != int(1e+15) else -1}") 
    
    