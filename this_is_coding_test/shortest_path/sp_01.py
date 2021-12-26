import heapq
import math
graph = {}

def dijkstra(v:int, e:int, start:int):
    # initialize distance list
    distance = [math.inf] * (v + 1)
    distance[start] = 0

    # initialize heapq and push start vertex
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, current = heapq.heappop(q)

        # skip lager distance and noexist edge
        if distance[current] < dist or current not in graph:
            continue
        
        # search liked vertex in current
        for vertex, weight in graph[current].items():
            # compute new cost
            cost = dist + weight
            # if new cost smaller than current cost, change value and push q vertex for search
            if cost < distance[vertex]:
                distance[vertex] = cost
                heapq.heappush(q, (cost, vertex))

    return distance


if __name__ == "__main__":
    vertex, edge = map(int, input().split())
    start = int(input())
    
    # initialize graph
    for i in range(edge):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = {}
        graph[u][v] = w

    distance = dijkstra(vertex, edge, start)

    for i in range(1, len(distance)):
        if distance[i] == math.inf:
            print("INF")
        else:
            print(distance[i])