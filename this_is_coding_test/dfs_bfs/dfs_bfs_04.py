from itertools import combinations
from copy import deepcopy
virus = []
empty = []

def dfs(n:int, m:int, lab:list, i:int, j:int, safty_count:int, visit:dict):
    visit[i*m + j] = True
    lab[i][j] = 2

    if available_check(n, m, i-1, j, lab, visit):
        safty_count = dfs(n, m, lab, i-1, j, safty_count-1, visit)

    if available_check(n, m, i+1, j, lab,  visit):
        safty_count = dfs(n, m, lab, i+1, j, safty_count-1, visit)

    if available_check(n, m, i, j-1,  lab, visit):
        safty_count = dfs(n, m, lab, i, j-1, safty_count-1, visit)

    if available_check(n, m, i, j+1,  lab, visit):
        safty_count = dfs(n, m, lab, i, j+1, safty_count-1, visit)

    return safty_count

def available_check(n:int, m:int, i:int, j:int, lab:list, visit:dict):
    if i < 0 or i >= n or j < 0 or j >= m or (i * m + j) in visit:
        return False

    if lab[i][j] != 0:
        return False

    return True

if __name__ == "__main__":
    n, m = map(int, input().split())
    lab = []
    for i in range(n):
        sub_lab = list(map(int, input().split()))
        lab.insert(i, sub_lab)
        for j in range(m):
            if sub_lab[j] == 0:
                empty.append(i*m + j)
            elif sub_lab[j] == 2:
                virus.append((i, j))
    wall_combination = list(combinations(empty, 3))

    max_safty_count = 0
    for walls in wall_combination:
        lab_copy = deepcopy(lab)
        lab_copy[walls[0]//m][walls[0]%m] = 1
        lab_copy[walls[1]//m][walls[1]%m] = 1
        lab_copy[walls[2]//m][walls[2]%m] = 1
        
        safty_count = len(empty) - 3
        visit = {}
        for i in range(n):
            for j in range(m):
                if lab_copy[i][j] == 2:
                    safty_count = dfs(n, m, lab_copy, i, j, safty_count, visit)
    
        max_safty_count = max(max_safty_count, safty_count)
    print(max_safty_count)
    
        