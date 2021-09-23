'''
board	skill	result
[[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	10
[[1,2,3],[4,5,6],[7,8,9]]	[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]	6

'''
from collections import defaultdict
def solution(board, skill):
    answer = 0

    sub_board_dict = defaultdict(int)
    row, col = len(board), len(board[0])
    for i in range(len(skill)):
        t, s_x, s_y, e_x, e_y, d = skill[i]
        if t == 1:
            d *= -1
        for x in range(s_x, e_x+1):
            for y in range(s_y, e_y+1):
                key = x * col + y
                # if key in sub_board_dict:
                sub_board_dict[key] += d
                # else:
                    # sub_board_dict[key] = d

    cnt = 0
    for key, value in sub_board_dict.items():
        x, y = key // col, key % col
        if (board[x][y] + value) <= 0:
            cnt += 1

    answer = len(board) * len(board[0]) - cnt

    return answer


def solution2(board, skill):
    answer = 0

    sub_board_dict = {}
    for i in range(len(skill)):
        t, s_x, s_y, e_x, e_y, d = skill[i]
        if t == 1:
            d *= -1
        for x in range(s_x, e_x+1):
            for y in range(s_y, e_y+1):
                if (x,y) in sub_board_dict:
                    sub_board_dict[(x,y)] += d
                else:
                    sub_board_dict[(x,y)] = d

    cnt = 0
    for key, value in sub_board_dict.items():
        x, y = key
        if (board[x][y] + value) <= 0:
            cnt += 1

    answer = len(board) * len(board[0]) - cnt

    return answer


if __name__ == "__main__":
    board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
    skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
    print(solution(board, skill))