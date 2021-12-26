INF = 1e+9

def floyd(graph:list, n:int):
    for k in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        graph[i][i] = 0

    for i in range(m):
        s, e = map(int, input().split())
        graph[s][e] = 1

    floyd(graph, n)

    student_cnt = 0
    for i in range(1, n+1):
        local_cnt = 0
        for j in range(1, n+1):
            if graph[i][j] != 0 and graph[i][j] != INF:
                local_cnt += 1
            if graph[j][i] != 0 and graph[j][i] != INF:
                local_cnt += 1

        if local_cnt == n -1:
            student_cnt += 1

    print(student_cnt)
