import sys
sys.stdin = open("samsung/sample_input.txt", "r")

"""
주요 아이디어
특정 행까지 배치가 완료되었을 때, 해당 행의 배치가 동일하면,
그 하단의 배치로 인해 만들어질 수 있는 최대 칩 갯수는 무조건 동일하다.
이를 DP로 Top-down 구성
"""

def dfs(i, j, cnt, masking):
    global max_count
    
    if j >= W - 1:
        max_count = max(max_count, cnt)
        return cnt
    
    if i >= H - 1:
        if dp[masking][j] >= cnt:
            return
        dp[masking][j] = cnt
        dfs(0, j+1, cnt, 0)
        return
    
    if wafer[i][j] == 0 and wafer[i+1][j] == 0 and wafer[i][j+1] == 0 and wafer[i+1][j+1] == 0:
        wafer[i][j] = wafer[i+1][j] = wafer[i][j+1] = wafer[i+1][j+1] = 1
        dfs(i+2, j, cnt+1, masking + 2**i)
        wafer[i][j] = wafer[i+1][j] = wafer[i][j+1] = wafer[i+1][j+1] = 0 # backtracking
    
    dfs(i+1, j, cnt, masking)
    
        


T = int(input())
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    wafer = [list(map(int, input().split())) for _ in range(H)]
    
    max_count = 0
    dp = [[-1] * W for _ in range(2 ** H + 1)]
    dfs(0, 0, 0, 0)
    print(f'#{test_case} {max_count}')


