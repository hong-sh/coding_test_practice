INF = 1e+9

def floyd(graph:list, v:int, start:int, x:int, k:int):
    for k in range(1, v+1):
        for s in range(1, v+1):
            for e in range(1, v+1):
                graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])
    
    min_cost = graph[start][k] + graph[k][x]
    return min_cost if min_cost < INF else -1

if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[INF]*(v+1) for _ in range(v+1)]

    for i in range(v+1):
        graph[i][i] = 0
    
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1

    x, k = map(int, input().split())
    cost = floyd(graph, v, 1, x, k)
    print(cost)