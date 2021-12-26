'''
https://programmers.co.kr/learn/courses/30/lessons/42894

board	result
[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]	2
[[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]] 3
'''

'''
x         x      x      x        x
xxx     xxx     xxx     x        x
                        xx      xx
'''
matching_case = {
    1: [[0,0], [1,0], [1,1], [1,2]],
    2: [[0,2], [1,0], [1,1], [1,2]],
    3: [[0,1], [1,0], [1,1], [1,2]],
    4: [[0,0], [1,0], [2,0], [2,1]],
    5: [[2,0], [0,1], [1,1], [2,1]]
}

valid_case = {
    1: [[1,1], [1,2]],
    2: [[1,0], [1,1]],
    3: [[1,0], [1,2]],
    4: [[2,1]],
    5: [[2,0]]
}

def find_match(i, j, board):
    match_num = -1
    for key, values in matching_case.items():
        standard = values[0]
        if (i+standard[0]) >= len(board) or (j+standard[1]) >= len(board) or board[i+standard[0]][j+standard[1]] == 0:
            continue

        match_stack = 0
        for value in values:
            if (i+value[0]) < len(board) and (j+value[1]) < len(board):
                if board[i+standard[0]][j+standard[1]] == board[i+value[0]][j+value[1]]:
                    match_stack += 1

        if match_stack == len(values):
            match_num = key

    return match_num

def del_valid(i, j, board, match_num):
    valid_stack = 0
    for value in valid_case[match_num]:
        valid = True
        for k in range(i+value[0]-1, -1, -1):
            if board[k][j+value[1]] != 0:
                valid = False
                break

        if valid:
            valid_stack += 1

    if valid_stack == len(valid_case[match_num]):
        return True

    return False
    
def del_block(i, j, board, match_num):
    for value in matching_case[match_num]:
        board[i+value[0]][j+value[1]] = 0

def solution(board):
    answer = 0

    change = True
    while change:
        change = False
        for i in range(len(board)):
            for j in range(len(board)):
                match_num = find_match(i, j, board)
                if match_num != -1:
                    if del_valid(i, j, board, match_num):
                        change = True
                        answer += 1
                        del_block(i, j, board, match_num)

    return answer


if __name__ == "__main__":
    board = \
    [[0,0,0,0,0,0,0,0,0,0]
    ,[0,0,0,2,2,0,0,0,0,0]
    ,[0,0,0,2,1,0,0,0,0,0]
    ,[0,0,0,2,1,0,0,0,0,0]
    ,[0,0,0,0,1,1,0,0,0,0]
    ,[0,0,0,0,0,0,0,0,0,0]]
    
    print(solution(board))