"""
4 4 1
1 2 10
2 4 10
1 3 1
3 4 100
"""


import sys
sys.stdin = open("practice/sample_input.txt", "r")

import sys
input = sys.stdin.readline

import heapq
from collections import deque

N, M, K = map(int, input().split())

graph_dict = {node:{} for node in range(N+1)}

for _ in range(M):
    u, v, w = map(int, input().split())
    graph_dict[u][v] = w
    graph_dict[v][u] = w
    
INF = sys.maxsize
distances = [[INF for _ in range(K+1)] for _ in range(N+1)]

def dijkstra(start):
    count = 0
    distances[start][count] = 0
    
    q = []
    heapq.heappush(q, [0, start, count])
    
    while q:
        dist, current, count = heapq.heappop(q)
        
        if distances[current][count] < dist:
            continue
        
        for next_node, next_dist in graph_dict[current].items():
            new_dist = next_dist + dist # 포장 안했을 경우
            if distances[next_node][count] > new_dist:
                distances[next_node][count] = new_dist
                heapq.heappush(q, [new_dist, next_node, count])
                
            if count < K and distances[next_node][count+1] > dist:
                distances[next_node][count+1] = dist
                heapq.heappush(q, [dist, next_node, count+1])
                    

dijkstra(1)
print(min(distances[N]))