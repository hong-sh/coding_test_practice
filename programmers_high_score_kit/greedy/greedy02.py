'''
https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3
name	return
"JEROEN"	56
"JAN"	23
'''

alphabet = {
    'A' : 0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9,
    'K' : 10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18,
    'T' : 19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25
}

def solution(name):
    answer = 0
    
    name = list(name)
    move = [0] * len(name)
    
    for i in range(len(name)):
        move[i] = min((alphabet[name[i]] , 26 - alphabet[name[i]]))    

    start = ["A"] * len(name)
    start_idx = 0
    while True:
        answer += move[start_idx]
        start[start_idx] = name[start_idx]

        if start == name:
            break

        r_idx = start_idx
        r_move = 0
        while start[r_idx] == name[r_idx]:
            r_idx = r_idx + 1 if r_idx < len(name) - 1 else 0
            r_move += 1
        
        l_idx = start_idx
        l_move = 0
        while start[l_idx] == name[l_idx]:
            l_idx = l_idx - 1 if l_idx > 0 else len(name) - 1
            l_move += 1

        start_idx = r_idx if r_move <= l_move else l_idx
        answer += min(r_move, l_move)
        
    # right_move = 0
    # start = ["A"] * len(name)
    # for i in range(len(name)):
    #     right_move += move[i]
    #     start[i] = name[i]
    #     if start == name:
    #         break
    #     right_move += 1
        
    # left_move = 0
    # start = ["A"] * len(name)
    # left_move += move[0]
    # start[0] = name[0]
    # for i in range(len(name)-1, 0, -1):
    #     left_move += 1
    #     left_move += move[i]
    #     start[i] = name[i]
    #     if start == name:
    #         break
    
    # answer = min(right_move, left_move)

    return answer