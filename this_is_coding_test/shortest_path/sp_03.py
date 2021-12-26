import heapq

graph = {}
INF = 1e+9

def dijkstra(n:int, start:int):
    distance = [INF] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, current = heapq.heappop(q)

        if distance[current] < dist or current not in graph:
            continue

        for v, w in graph[current].items():
            cost = distance[current] + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

    return distance
 

if __name__ == "__main__":
    n, m, c = map(int, input().split())
    for _ in range(m):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = {}
        graph[u][v] = w

    distance = dijkstra(n, c)
    cnt = 0
    max_cost = 0
    for i in range(len(distance)):
        if distance[i] != INF and distance[i] != 0:
            cnt += 1
            max_cost = max(max_cost, distance[i])

    print(cnt, ' ', max_cost)

    