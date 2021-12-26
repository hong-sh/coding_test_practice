def get_ice_count(n:int, m:int, ice_frame:list):
    stack = []
    count = 0
    for i in range(n):
        for j in range(m):
            if ice_frame[i][j] == '0':
                stack = [(i, j)]
                ice_frame[i][j] = '2'
                while len(stack) != 0:
                    row, col = stack.pop()
                    if row - 1 >= 0:
                        search(row-1, col, ice_frame, stack)
                    if row + 1 <= n - 1:
                        search(row+1, col, ice_frame, stack)
                    if col - 1 >= 0:
                        search(row, col-1, ice_frame, stack)
                    if col + 1 <= m - 1:
                        search(row, col+1, ice_frame, stack)
                count += 1
    return count

def search(row:int, col:int, ice_frame:list, stack:list):
    if ice_frame[row][col] == '0':
        ice_frame[row][col] = '2'
        stack.append((row, col))

if __name__ == "__main__":
    ice_frame = []
    n, m = map(int, input().split())
    for i in range(n):
        state = input()
        row = []
        for j in range(m):
            row.insert(j, state[j])
        ice_frame.insert(i, row)
    print(get_ice_count(n, m, ice_frame))
