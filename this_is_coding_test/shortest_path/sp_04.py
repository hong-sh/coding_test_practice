INF = 1e+9

def floyd(graph:list, n:int):
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])

    

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        graph[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)

    floyd(graph, n)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > INF:
                graph[i][j] = 0
            print(graph[i][j], end=' ')
        print()