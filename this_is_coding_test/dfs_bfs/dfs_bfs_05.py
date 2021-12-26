from queue import deque

virus_map = []
virus_queue = []
n = 0

def bfs(q:deque, i:int):
    local_queue = deque()
    while len(q) != 0:
        x, y = q.popleft()
        if available_check(x, y-1):
            virus_map[x][y-1] = i+1
            local_queue.append((x, y-1))
        if available_check(x, y+1):
            virus_map[x][y+1] = i+1
            local_queue.append((x, y+1))
        if available_check(x-1, y):
            virus_map[x-1][y] = i+1
            local_queue.append((x-1, y))
        if available_check(x+1, y):
            virus_map[x+1][y] = i+1
            local_queue.append((x+1, y))

    return local_queue


def available_check(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    
    if virus_map[x][y] != 0:
        return False

    return True

if __name__ == "__main__":
    n, k = map(int, input().split())
    for i in range(k):
        virus_queue.append(deque())

    for i in range(n):
        sub = list(map(int, input().split()))
        virus_map.insert(i, sub)
        for j in range(n):
            if sub[j] != 0:
                virus_queue[sub[j]-1].append((i, j))

    s, x, y = map(int, input().split())
    time = 0
    while time < s:
        for i in range(k):
            virus_queue[i] = bfs(virus_queue[i], i)
        time += 1
    
    print(virus_map[x-1][y-1])
