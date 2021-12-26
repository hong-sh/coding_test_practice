'''
https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
'''
def solution(prices):
    answer = []
    for i in range(len(prices)):
        dec = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                dec = j
                break
        rg = 0
        if dec == 0:
            rg = len(prices) - i - 1
        else:
            rg = dec - i
        answer.append(rg)
    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))