
from typing import List
import heapq
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph_dict = {node : {} for node in range(n)}
        
        for flight in flights:
            from_, to_, price_ = flight[0], flight[1], flight[2]
            graph_dict[from_][to_] = price_
            
            
        INF = 1e+15
        def dijkstra(start):
            #distances = [[] for _ in range(n)]
            distances = [INF] * n
            #q = []
            q = deque([(start, 0, 0)])
            #heapq.heappush(q, (start, 0, 0))
            distances[start] = 0
            
            while q:
                current, dist, stop = q.popleft() #heapq.heappop(q)
                    
                if stop >= k+1:
                    continue
                
                #if distances[current] < dist:
                #    continue
                
                for next_node, next_dist in graph_dict[current].items():
                       
                    new_dist = dist + next_dist
                    if distances[next_node] > new_dist:
                        #distances[next_node].append(new_dist)
                        distances[next_node] = new_dist
                        q.append((next_node, new_dist, stop+1))
                        #heapq.heappush(q, (next_node, new_dist, stop+1))
                
            return distances
        
        distances = dijkstra(src)
        
        #if len(distances[dst]) == 0:
        if distances[dst] == INF:
            return -1
        
        return distances[dst]
        #return min(distances[dst])
    
sol = Solution()
print(sol.findCheapestPrice(n = 5, flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1],[3,4,1]], src = 0, dst = 4, k = 2))