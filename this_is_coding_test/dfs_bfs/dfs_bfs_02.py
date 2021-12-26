from collections import deque

def get_cost(n:int, m:int, route:list):
    cost = 1
    queue = deque()
    route[0][0] = -1
    queue.append((0, 0, cost))
    while True:
        row, col, cost = queue.popleft()
        if row == n-1 and col == m-1:
            return cost

        if row - 1 >= 0:
            search(row-1, col, route, queue, cost+1)
        if row + 1 <= n - 1:
            search(row+1, col, route, queue, cost+1)
        if col - 1 >= 0:
            search(row, col-1, route, queue, cost+1)
        if col + 1 <= m - 1:
            search(row, col+1, route, queue, cost+1)

def search(row:int, col:int, route:list, queue:object, cost:int):
    if route[row][col] == 1:
        route[row][col] = -1
        queue.append((row, col, cost))


if __name__ == "__main__":
    route = []
    n, m = map(int, input().split())
    for i in range(n):
        row_route = input()
        row = []
        for j in range(m):
            row.insert(j, int(row_route[j]))
        route.insert(i, row)
    print(get_min_cost(n, m, route))