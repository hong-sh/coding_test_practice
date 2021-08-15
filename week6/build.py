'''
https://programmers.co.kr/learn/courses/30/lessons/60061

n	build_frame	result
5	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
5	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]

'''

from copy import deepcopy

def impassible_check(build_state):
    for x, y, a in build_state:
        if a == 0:
            if y != 0 and (x-1, y, 1) not in build_state and (x, y, 1) not in build_state \
                and (x, y-1, 0) not in build_state:
                return True
        else:
            if (x, y-1, 0) not in build_state and (x+1, y-1, 0) not in build_state \
                and not ((x-1, y, 1) in build_state and (x+1, y, 1) in build_state):
                return True

    return False
        

def solution(n, build_frame):
    answer = [[]]

    build_state = set()
    for build in build_frame:
        # 0 col 1 row
        # 0 del 1 build
        item = (build[0], build[1], build[2])
        if build[3] == 1:
            build_state.add(item)
            if impassible_check(build_state):
                build_state.remove(item)

        elif build[3] == 0:
            build_state.remove(item)
            if impassible_check(build_state):
                build_state.add(item)

    build_state = map(list, build_state)
    answer = sorted(build_state, key=lambda x : (x[0], x[1], x[2]))
    return answer

    
def build_col_val(n, build_state, x, y):
    valid = False
    if y == 0 or list([x-1, y, 1]) in build_state or list([x, y, 1]) in build_state \
        or list([x, y-1, 0]) in build_state:
        valid = True

    return valid

def build_row_val(n, build_state, x, y):
    valid = False
    if list([x, y-1, 0]) in build_state or list([x+1, y-1, 0]) in build_state \
        or (list([x-1, y, 1]) in build_state and list([x+1, y, 1]) in build_state):
        valid = True

    return valid

def del_col_val(n, build_state, x, y):
    valid = True

    copy_state = deepcopy(build_state)
    for i in range(len(copy_state)):
        if x == copy_state[i][0] and y == copy_state[i][1] and 0 == copy_state[i][2]:
            break
    del copy_state[i]

    for build in copy_state:
        # if abs(build[0] - x) <= 1 and abs(build[1] - y) <= 1:
        if build[2] == 0:
            if build_col_val(n, copy_state, build[0], build[1]) == False:
                return False
        elif build[2] == 1:
            if build_row_val(n, copy_state, build[0], build[1]) == False:
                return False
    
    return valid

def del_row_val(n, build_state, x, y):
    valid = True

    copy_state = deepcopy(build_state)
    for i in range(len(copy_state)):
        if x == copy_state[i][0] and y == copy_state[i][1] and 0 == copy_state[i][2]:
            break
    del copy_state[i]

    for build in copy_state:
        # if abs(build[0] - x) <= 1 and abs(build[1] - y) <= 1:
        if build[2] == 0:
            if build_col_val(n, copy_state, build[0], build[1]) == False:
                return False
        elif build[2] == 1:
            if build_row_val(n, copy_state, build[0], build[1]) == False:
                return False
    
    return valid

def solution2(n, build_frame):
    answer = [[]]

    build_state = set()
    for build in build_frame:
        # 0 col 1 row
        # 0 del 1 build

        valid = False
        if build[2] == 0 and build[3] == 0:
            valid = del_col_val(n, build_state, build[0], build[1])
        if build[2] == 0 and build[3] == 1:
            valid = build_col_val(n, build_state, build[0], build[1])
        if build[2] == 1 and build[3] == 0:
            valid = del_row_val(n, build_state, build[0], build[1])
        if build[2] == 1 and build[3] == 1:
            valid = build_row_val(n, build_state, build[0], build[1])

        if valid and build[3] == 1:
            build_state.append([build[0], build[1], build[2]])

        if valid and build[3] == 0:
            for i in range(len(build_state)):
                if build[0] == build_state[i][0] and build[1] == build_state[i][1] and build[2] == build_state[i][2]:
                    break
            del build_state[i]

    answer = sorted(build_state, key=lambda x : (x[0], x[1], x[2]))
    return answer

if __name__ == "__main__":
    n = 5
    build_fame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    build_fame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

    print(solution(n, build_fame))