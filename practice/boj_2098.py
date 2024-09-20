import sys
sys.stdin = open("practice/sample_input.txt", "r")

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

weights = [list(map(int, input().split())) for _ in range(N)]
dp = {}
INF = 1e+15

def dfs(current, visited):
    if visited == ( 1 << N) -1 :
        if weights[current][0] != 0:
            return weights[current][0]
        else:
            return INF
    
    if (current, visited) in dp:
        return dp[(current, visited)]
    
    min_cost = INF
    for i in range(N):
        if weights[current][i] == 0 or visited & (1 << i):
            continue
        
        cost = dfs(i, visited | (1 << i)) + weights[current][i]
        min_cost = min(min_cost, cost)
        
    dp[(current, visited)] = min_cost
    return min_cost

print(dfs(0, 1))