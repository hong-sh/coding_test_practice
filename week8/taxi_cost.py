'''

https://programmers.co.kr/learn/courses/30/lessons/72413

n	s	a	b	fares	result
6	4	6	2	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	82
7	3	4	1	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	14
6	4	5	6	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]	18
'''
import heapq

INF = int(1e9)

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(n, s, a, b, fares):
    answer = 0

    graph = [[] for i in range(n+1)]
    distance = [[INF] * (n+1) for i in range(n+1)]

    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
        
    for i in range(1, n+1):
        dijkstra(i, graph, distance[i])
    

    min_cost = INF
    for i in range(1, n+1):
        min_cost = min(distance[s][i] + distance[i][a] + distance[i][b], min_cost)

    return min_cost


if __name__ == "__main__":
    n = 6
    s = 4
    a = 5
    b = 6

    fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
    print(solution(n, s, a, b, fares))