import heapq

INF = int(1e+9)

def dijkstra(graph:list, n:int):
    cost_graph = [[INF] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (graph[0][0], [0,0]))

    while q:
        cost, pos = heapq.heappop(q)

        if cost_graph[pos[0]][pos[1]] < cost:
            continue

        if pos[0] - 1 >= 0: # left
            new_cost = cost + graph[pos[0]-1][pos[1]] if cost_graph[pos[0]-1][pos[1]] == INF \
                 else cost + cost_graph[pos[0]-1][pos[1]]
            if new_cost < cost_graph[pos[0]-1][pos[1]]:
                cost_graph[pos[0]-1][pos[1]] = new_cost
                heapq.heappush(q, (new_cost, [pos[0]-1, pos[1]]))

        if pos[0] + 1 < n: # right
            new_cost = cost + graph[pos[0]+1][pos[1]] if cost_graph[pos[0]+1][pos[1]] == INF \
                else cost + cost_graph[pos[0]+1][pos[1]]
            if new_cost < cost_graph[pos[0]+1][pos[1]]:
                cost_graph[pos[0]+1][pos[1]] = new_cost
                heapq.heappush(q, (new_cost, [pos[0]+1, pos[1]]))

        if pos[1] - 1 >= 0: # top
            new_cost = cost + graph[pos[0]][pos[1]-1] if cost_graph[pos[0]][pos[1]-1] == INF \
                else cost + cost_graph[pos[0]][pos[1]-1]
            if new_cost < cost_graph[pos[0]][pos[1]-1]:
                cost_graph[pos[0]][pos[1]-1] = new_cost
                heapq.heappush(q, (new_cost, [pos[0], pos[1]-1]))

        if pos[1] + 1 < n: # down
            new_cost = cost + graph[pos[0]][pos[1]+1] if cost_graph[pos[0]][pos[1]+1] == INF \
                else cost + cost_graph[pos[0]][pos[1]+1]
            if new_cost < cost_graph[pos[0]][pos[1]+1]:
                cost_graph[pos[0]][pos[1]+1] = new_cost
                heapq.heappush(q, (new_cost, [pos[0], pos[1]+1]))

    return cost_graph[n-1][n-1]        


if __name__ == "__main__":
    n = int(input())
    graph = []

    for i in range(n):
        sub_graph = list(map(int, input().split()))
        graph.insert(i, sub_graph)

    print(dijkstra(graph, n))