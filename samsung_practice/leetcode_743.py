
from typing import List
from collections import deque
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph_dict = {node: {} for node in range(1, n+1)}
        for time in times:
            u, v, w = time[0], time[1], time[2]
            graph_dict[u][v] = w
        
        INF = 1e+15 
        
        def dijkstra(start):
            distances = [INF] * (n+1)
            q = []
            heapq.heappush(q, (start, 0))
            distances[start] = 0
            
            while q:
                current, dist = heapq.heappop(q)
                
                if distances[current] < dist:
                    continue
                
                for next_node, next_dist in graph_dict[current].items():
                    new_dist = dist + next_dist
                    if new_dist < distances[next_node]:
                        distances[next_node] = new_dist
                        heapq.heappush(q, (next_node, new_dist))
                        
            return distances
                     
        distances = dijkstra(k)
        max_dist = max(distances[1:])
        if max_dist >= INF:
            return -1
        
        return max_dist
    
    
sol = Solution()
print(sol.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
                    