def dfs(n:int, m:int, x:int, visit:list, adj_matrix:list, cost:int):
    for i in range(n):
        if adj_matrix[x][i] == 1:
            if visit[i] == 0:
                visit[i] = cost
            else:
                visit[i] = min(visit[i], cost)
            dfs(n, m, i, visit, adj_matrix, cost + 1)
    
if __name__ == "__main__":
    n, m, k, x = map(int, input().split())
    visit = [0] * n
    adj_matrix = []
    for i in range(n):
        adj_matrix.insert(i, [0] * n)
    
    for i in range(m):
        start, end = map(int, input().split())
        adj_matrix[start-1][end-1] = 1
    
    dfs(n, m, 0, visit, adj_matrix, 1)
    city_list = []
    for i in range(m):
        if visit[i] == k:
            print(i+1)
            city_list.append(i+1)
    
    if len(city_list) == 0:
        print(-1)
