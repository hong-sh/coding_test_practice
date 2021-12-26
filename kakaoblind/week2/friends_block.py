def solution(m, n, board):
    answer = 0
    change = True
    while change:
        change = False
        change_idxs = []
        for j in range(m-1):
            for i in range(n-1):
                sub_set = set([board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]])
                if len(sub_set) == 1 and "0" not in sub_set:
                    change = True
                    change_idxs.append((i, j))
        
        if change:
            for change_idx in change_idxs:
                i, j = change_idx[0], change_idx[1]
                board[i][j], board[i+1][j], board[i][j+1], board[i+1][j+1] = "0", "0", "0", "0"

            stack = [[] * n]
            for i in range(n):
                for j in range(m-1, 0, -1):
                    if board[i][j] != "0":
                        stack.append(board[i][j])
            
            for i in range(n):
                for j in range(m):
                    if len(stack[i]) == m-j:
                        board[i][j] = stack[i].pop()
                    else:
                        board[i][j] = "0"

    for i in range(n):
        for j in range(m):
            if board[i][j] == "0":
                answer += 1


    return answer


if __name__ == "__main__":
    m, n = 4, 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    print(solution(m, n, board))