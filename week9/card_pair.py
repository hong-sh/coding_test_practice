'''

https://programmers.co.kr/learn/courses/30/lessons/72415

board	r	c	result
[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]	1	0	14
[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]	0	1	16
'''

def get_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def solution(board, r, c):
    answer = 0

    pos_dict = {}
    cnt_dict = {}
    visit_dict = {}

    card_cnt = 0
    min_dist = 999
    target_card = None
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0:
                card = board[i][j]

                if card in pos_dict:
                    pos_dict[card].append((i, j))
                    x1, y1 = pos_dict[card][0]
                    x2, y2 = pos_dict[card][1]
                    cnt_dict[card] = get_dist(x1, y1, x2, y2) + 2
                else:
                    pos_dict[card] = [(i, j)]
                    card_cnt += 1

                dist_from_rc = get_dist(r, c, i, j) 
                if min_dist > dist_from_rc:
                    min_dist = dist_from_rc
                    target_card = (card, i, j)

    while card_cnt > 1:
        card, i, j = target_card
        visit_dict[card] = True

        answer += get_dist(r, c, i, j) + cnt_dict[card]
        
        px1, py1 = pos_dict[card][0]
        px2, py2 = pos_dict[card][1]

        if px1 == i and py1 == j:
            r, c = px1, py1
        else:
            r, c = px2, py2

        min_dist = 999
        for key, values in pos_dict.items():
            if key in visit_dict:
                continue
            
            for value in values:
                x, y = value
                dist_from_rc = get_dist(r, c, x, y)
                if min_dist > dist_from_rc:
                    min_dist = dist_from_rc
                    target_card = (key, x, y)
        card_cnt -= 1

    return answer


if __name__ == "__main__":
    board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
    r = 0
    c = 1
    print(solution(board, r, c))

