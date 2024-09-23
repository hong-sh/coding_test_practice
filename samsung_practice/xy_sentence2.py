
import sys
sys.stdin = open("samsung/sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def dfs(sentence, goal_sentence, memo):
    if len(sentence) == len(goal_sentence):
        return sentence == goal_sentence
    
    #if sentence in memo:
    #    return memo[sentence]
    
    #sentence1 = sentence + 'X'
    #sentence2 = sentence + 'Y'
    #sentence2 = sentence2[::-1]
    
    is_possible = False
    if goal_sentence[0] == 'Y':
        is_possible = is_possible or dfs(sentence, goal_sentence[::-1][:-1], memo)
    if goal_sentence[-1] == 'X':
        is_possible = is_possible or dfs(sentence, goal_sentence[:-1], memo)
    
    #is_possible = dfs(sentence, goal_sentence, memo) or dfs(sentence, goal_sentence, memo)
    #memo[sentence] = is_possible
    return is_possible


for test_case in range(1, T + 1):
    S = input().strip()
    E = input().strip()
    
    memo = {}
    rst = dfs(S, E, memo)
    rst = "Yes" if rst else "No"
    print(f"#{test_case} {rst}")
    