import heapq

graph = {}
INF = int(1e+9)

def dijkstra(start:int, n:int):
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
    n, m = map(int, input().split())

    for i in range(m):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}

        graph[a][b] = 1
        graph[b][a] = 1


    distance = dijkstra(1, n)

    max_dist = 0
    max_idx = 0
    max_cnt = 0
    for i in range(len(distance)-1, 0, -1):
        if max_dist < distance[i] and distance[i] != INF:
            max_dist = distance[i]
            max_idx = i
            max_cnt = 1
        elif max_dist == distance[i]:
            max_idx = i
            max_cnt += 1


    print(max_idx, ' ', max_dist, ' ', max_cnt)