'''
n	k	result
437674	3	3
110011	10	2

'''

import math 

def solution(n, k):
    answer = 0

    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    base = rev_base[::-1] 
    splitted_n = base.split('0')
    for i in range(len(splitted_n)):
        if len(splitted_n[i]) == 0:
            continue
        is_prime = True
        check_num = int(splitted_n[i])
        if check_num == 1:
            continue
        for j in range(2, int(math.sqrt(check_num))+1):
            if check_num % j == 0:
                is_prime = False
        answer = answer + 1 if is_prime else answer
    return answer

if __name__ == "__main__":
    n = 437674
    k = 3
    print(solution(n, k))
    