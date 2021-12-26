import math
import heapq

'''
25.0 100.0
190.0 57.5
4
125.0 67.5
75.0 125.0
45.0 72.5
185.0 102.5
'''
INF = 1e+9

def distance(x:float, y:float, dest_x:float, dest_y:float):
    return math.sqrt((dest_x - x)**2 + (dest_y - y)**2)

def dijkstra(cost_graph:list, start:int, n:int):
    cost = [INF] * (n+2)
    cost[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        time, v = heapq.heappop(q)

        if cost[v] < time:
            continue

        for e, w in cost_graph[v]:
            new_cost = time + w
            if new_cost < cost[e]:
                cost[e] = new_cost
                heapq.heappush(q, (new_cost, e))

    return cost

if __name__ == "__main__":
    posX, posY = map(float, input().split())
    destX, destY = map(float, input().split())

    n = int(input())

    positions = []
    positions.append((posX, posY))

    cost_graph = [[] for _ in range(n+2)]
    for i in range(1, n+1):
        shooterX, shooterY = map(float, input().split())
        positions.append((shooterX, shooterY))

        dist_from_init = distance(posX, posY, shooterX, shooterY)
        cost_graph[0].append([i, dist_from_init/5])
    
    positions.append((destX, destY))
    cost_graph[0].append([n+1, distance(posX, posY, destX, destY)/5])

    for i in range(1, n+1):
        shooterX, shooterY = positions[i]
        for j in range(n+2):
            destX, destY = positions[j]
            distance_from_shooter = distance(shooterX, shooterY, destX, destY)
            if i != j:
                cost_graph[i].append([j, abs(distance_from_shooter - 50)/5 + 2])

    cost = dijkstra(cost_graph, 0, n)
    print(cost[n+1])
    
