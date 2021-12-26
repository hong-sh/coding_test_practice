import sys
input = sys.stdin.readline

def dfs(i:int, j:int, k:int, count:int, visit:list):
    if count > w + h:
        return -1

    if i+1 == w and j+1 == h:
        return count

    visit[i][j] = 1
    min_count = 999

    if k > 0 : # horse move
        if available_check(i-2, j-1, visit): 
            local_count = dfs(i-2, j-1, k-1, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count # min count check
        if available_check(i-2, j+1, visit):
            local_count = dfs(i-2, j+1, k-1, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count
        if available_check(i-1, j+2, visit):
            local_count = dfs(i-1, j+2, k-1, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count
        if available_check(i+1, j+2, visit):
            local_count = dfs(i+1, j+2, k-1, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count
        if available_check(i+2, j-1, visit):
            local_count = dfs(i+2, j-1, k-1, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count
        if available_check(i+2, j+1, visit):
            local_count = dfs(i+2, j+1, k-1, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count
        if available_check(i-1, j-2, visit):
            local_count = dfs(i-1, j-2, k-1, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count
        if available_check(i+1, j-2, visit):
            local_count = dfs(i+1, j-2, k-1, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count
    else: # monkey move
        if available_check(i-1, j, visit):
            local_count = dfs(i-1, j, k, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count
        if available_check(i, j+1, visit):
            local_count = dfs(i, j+1, k, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count
        if available_check(i+1, j, visit):
            local_count = dfs(i+1, j, k, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count
        if available_check(i, j-1, visit):
            local_count = dfs(i, j-1, k, count+1, visit)
            min_count = min(local_count, min_count) if local_count != -1 else min_count

    if min_count == 999:
        return -1

    return min_count

def available_check(i:int, j:int, visit:list): # available move check
    if i < 0 or j < 0 or i >= w or j >=h:
        return False

    if world[i][j] == 1 or visit[i][j] == 1:
        return False

    return True

k = int(input())
w, h = map(int, input().split())
visit = []
world = []
for i in range(w):
    sub_world = list(map(int, input().split()))
    world.insert(i, sub_world)
    visit.insert(i, [0] * h)

print(dfs(0, 0, k, 0, visit))
