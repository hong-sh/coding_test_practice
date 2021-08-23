'''
board                                                                   result
[[0,0,0,1,1], [0,0,0,1,0], [0,1,0,1,1], [1,1,0,0,1], [0,0,0,0,0]]       7
'''
from copy import deepcopy
from collections import deque

clock_rotate = {1:[[1, 0], [1, -1]], 2:[[0, -1], [-1,-1]], 3:[[-1, 0], [-1, 1]], 4:[[0, 1], [1, 1]]}
reverse_rotate = {1:[[-1, 0], [-1, -1]], 2:[[0,1], [-1,1]], 3:[[1,0], [1,1]], 4:[[-1,-1], [1,-1]]}
move_front = {1:[0,1], 2:[1,0], 3:[0,-1], 4:[-1,0]}
reverse_table = {1:3, 2:4, 3:1, 4:2}

def valid_block(x, y, board_size):
    if x >= 0 and y >= 0 and x < board_size and y < board_size:
        return True

    return False

def can_rotate(board, robot_pos, flag): # 0 : clock, 1 : reverse
    pos = None
    board_size = len(board)
    if flag == 0:
        rotate_table = clock_rotate[robot_pos[2]]
        x1, y1, x2, y2 = robot_pos[1][0] + rotate_table[0][0], robot_pos[1][1] + rotate_table[0][1], robot_pos[1][0] + rotate_table[1][0], robot_pos[1][1] + rotate_table[1][1]
        
        if not valid_block(x1, y1, board_size) or not valid_block(x2, y2, board_size):
            return False, pos

        if board[x1][y1] == 1 or board[x2][y2] == 1:
            return False, pos
        rotate = robot_pos[2] + 1
        rotate = 1 if rotate > 4 else rotate
        pos = [robot_pos[0], [x2, y2], rotate]

    else:
        rotate_table = reverse_rotate[robot_pos[2]]
        x1, y1, x2, y2 = robot_pos[1][0] + rotate_table[0][0], robot_pos[1][1] + rotate_table[0][1], robot_pos[1][0] + rotate_table[1][0], robot_pos[1][1] + rotate_table[1][1]
        if not valid_block(x1, y1, board_size) or not valid_block(x2, y2, board_size):
            return False, pos
        if board[x1][y1] == 1 or board[x2][y2] == 1:
            return False, pos
        rotate = robot_pos[2] - 1
        rotate = 4 if rotate < 1 else rotate
        pos = [robot_pos[0], [x2, y2], rotate]

    return True, pos

def can_move_front(board, robot_pos):
    pos = None
    move_table = move_front[robot_pos[2]]
    x, y = robot_pos[1][0] + move_table[0], robot_pos[1][1] + move_table[1]
    if not valid_block(x, y, len(board)):
        return False, pos
    if board[x][y] == 1:
        return False, pos

    pos = [robot_pos[1], [x,y], robot_pos[2]]
    return True, pos

def can_move_left(board, robot_pos):
    pos = None
    board_size = len(board)
    dx, dy = [-1, 0]
    x1, y1, x2, y2 = robot_pos[0][0] + dx, robot_pos[0][1] + dy, robot_pos[1][0] + dx, robot_pos[1][1] + dy
    if not valid_block(x1, y1, board_size) or not valid_block(x2, y2, board_size):
        return False, pos
    if board[x1][y1] == 1 or board[x2][y2] == 1:
        return False, pos
    pos = [[x1, y1], [x2, y2], robot_pos[2]]
    return True, pos

def can_move_right(board, robot_pos):
    pos = None
    board_size = len(board)
    dx, dy = [1, 0]
    x1, y1, x2, y2 = robot_pos[0][0] + dx, robot_pos[0][1] + dy, robot_pos[1][0] + dx, robot_pos[1][1] + dy
    if not valid_block(x1, y1, board_size) or not valid_block(x2, y2, board_size):
        return False, pos
    if board[x1][y1] == 1 or board[x2][y2] == 1:
        return False, pos
    pos = [[x1, y1], [x2, y2], robot_pos[2]]
    return True, pos

def bfs(board, visit, robot_pos, time):
    dest = len(board) - 1
    
    q = deque()
    q.append([robot_pos, time])

    while q:
        robot_pos, time = q.popleft()
        robot_reverse_pos = [robot_pos[1], robot_pos[0], reverse_table[robot_pos[2]]]
        visit[robot_pos[0][0]][robot_pos[0][1]], visit[robot_pos[1][0]][robot_pos[1][1]] = 2, 2
        if [dest, dest] in robot_pos:
            return time

        is_can_rotate_clock, clock_pos = can_rotate(board, robot_pos, 0)
        if is_can_rotate_clock and visit[clock_pos[1][0]][clock_pos[1][1]] != 2:
            q.append([clock_pos, time+1])

        is_can_rotate_reverse, reverse_pos = can_rotate(board, robot_pos, 1)
        if is_can_rotate_reverse and visit[reverse_pos[1][0]][reverse_pos[1][1]] != 2:
            q.append([reverse_pos, time+1])

        is_can_move_front, move_pos_front = can_move_front(board, robot_pos)
        if is_can_move_front and visit[move_pos_front[1][0]][move_pos_front[1][1]] != 2:
            q.append([move_pos_front, time+1])

        is_can_move_left, move_pos_left = can_move_left(board, robot_pos)
        if is_can_move_left and visit[move_pos_left[1][0]][move_pos_left[1][1]] != 2:
            q.append([move_pos_left, time+1])
            
        is_can_move_right, move_pos_right = can_move_left(board, robot_pos)
        if is_can_move_right and visit[move_pos_right[1][0]][move_pos_right[1][1]] != 2:
            q.append([move_pos_right, time+1])

        is_can_rotate_clock, reverse_clock_pos = can_rotate(board, robot_reverse_pos, 0)
        if is_can_rotate_clock and visit[reverse_clock_pos[1][0]][reverse_clock_pos[1][1]] != 2:
            q.append([reverse_clock_pos, time+1])

        is_can_rotate_reverse, reverse_reverse_pos = can_rotate(board, robot_reverse_pos, 1)
        if is_can_rotate_reverse and visit[reverse_reverse_pos[1][0]][reverse_reverse_pos[1][1]] != 2:
            q.append([reverse_reverse_pos, time+1])

        is_can_move_front, reverse_move_pos_front = can_move_front(board, robot_reverse_pos)
        if is_can_move_front and visit[reverse_move_pos_front[1][0]][reverse_move_pos_front[1][1]] != 2:
            q.append([reverse_move_pos_front, time+1])

    return -1

def solution(board):
    answer = 0
    robot_pos = [[0,0], [0,1], 1]
    visit = deepcopy(board)
    min_time = bfs(board, visit, robot_pos, 0)

    return min_time

if __name__ == "__main__":
    board = [[0,0,0,1,1], [0,0,0,1,0], [0,1,0,1,1], [1,1,0,0,1], [0,0,0,0,0]]
    print(solution(board))