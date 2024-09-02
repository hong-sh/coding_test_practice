
from collections import deque

def solution(n, results):
    answer = 0
    
    win_dict = {i: [] for i in range(1, n+1)}
    lose_dict = {i: [] for i in range(1, n+1)}
    
    for result in results:
        winner, loser = result[0], result[1]
        win_dict[winner].append(loser)
        lose_dict[loser].append(winner)
        
    for i in range(1, n+1):
        queue = deque()
        queue.append(i)
        
        visited = [0] * (n+1)
        visited[i] = 1
        count = 0
        while queue:
            now = queue.popleft()
            visited[now] = 1    
            for next_player in lose_dict[now]:
                if visited[next_player] == 0 and next_player not in win_dict[i]:
                    count += 1
                    queue.append(next_player)
        
        if len(win_dict[i]) + count == n-1:
            answer += 1
        
    return answer


n, results = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
