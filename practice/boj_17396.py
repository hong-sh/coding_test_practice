
import sys
sys.stdin = open("practice/sample_input.txt", "r")

import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
sights = list(map(int, input().split()))
sights[-1] = 0

graph_dict = {i : {} for i in range(N)}
for _ in range(M):
    a, b, t = map(int, input().split())
    
    if sights[a] == 1 or sights[b] == 1:
        continue
    
    graph_dict[a][b] = t
    graph_dict[b][a] = t
    
INF = 1e+10
    

def dijkstra(start):
    distances = [INF] * N
    q = []
    distances[start] = 0
    heapq.heappush(q, (start, 0))
    
    while q:
        current, dist = heapq.heappop(q)
        
        if distances[current] < dist:
            continue
        
        for next_v, next_d in graph_dict[current].items():
            new_dist = dist + next_d
            if distances[next_v] > new_dist:
                distances[next_v] = new_dist
                heapq.heappush(q, (next_v, new_dist))
                
    return distances

distances = dijkstra(0)
answer = distances[N-1]
if answer >= INF:
    answer = -1
    
print(answer)