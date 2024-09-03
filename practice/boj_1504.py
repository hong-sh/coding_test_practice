"""
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
"""

import sys
sys.stdin = open("practice/sample_input.txt", "r")


import heapq

V, E = map(int, input().split())
graph_dict = {i+1:{} for i in range(V)}
for _ in range(E):
    s, e, w = map(int, input().split())
    graph_dict[s][e] = w
    graph_dict[e][s] = w
    
def bfs(start):
    queue = []
    distances = [float('inf')] * (V+1)
    distances[start] = 0
    heapq.heappush(queue, (start, 0))

    while queue:
        current, dist = heapq.heappop(queue)
        
        if distances[current] < dist:
            continue
        
        for next_v, next_d in graph_dict[current].items():
            new_dist = dist + next_d
            if distances[next_v] > new_dist:
                distances[next_v] = new_dist
                heapq.heappush(queue, (next_v, new_dist))
                
    return distances

#total_dist = [[float('inf') for _ in range(V+1)] for _ in range(V+1)]
V1, V2 = map(int, input().split())

dist1 = bfs(V1)
dist2 = bfs(V2)

#for i in range(V):
#    total_dist[i+1] = bfs(i+1)

total_dist = min(dist1[1] + dist1[V2] + dist2[V], dist2[1] + dist2[V1] + dist1[V])
if total_dist >= float('inf'):
    total_dist = -1

print(total_dist)
    
        
        