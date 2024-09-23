import sys
sys.stdin = open("samsung/sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

valid_dict = {
    0 : [1, 4, 6], # LEFT
    1 : [2, 5, 6], # UP
    2 : [1, 3, 5], # RIGHT
    3 : [2, 3, 4], # DOWN
}

block_direction_dict = {
    1 : [[1, 4, 6], [1, 3, 5]], # LEFT, RIGHT
    2 : [[2, 5, 6], [2, 3, 4]], # UP, DOWN
    3 : [[1, 4, 6], [2, 5, 6]], # LEFT, UP
    4 : [[2, 5, 6], [1, 3, 5]], # UP, RIGHT
    5 : [[1, 4, 6], [2, 3, 4]], # LEFT, DOWN
    6 : [[1, 3, 5], [2, 3, 4]], # RIGHT, DOWN
}

move_dict = {
    0 : [0, -1],
    1 : [-1, 0],
    2 : [0, 1],
    3 : [1, 0],
}

def valid_check(x, y, block_direction):
    dx, dy = x + move_dict[block_direction][0], y + move_dict[block_direction][1]
    

def dfs(x, y, cnt):
    if x == N-1 and y == N-1:
        
        return cnt
    
    

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    