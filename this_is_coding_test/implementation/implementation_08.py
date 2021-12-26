
import copy

action_dict = {'R': [0, 1], 'L': [0,-1], 'U': [-1, 0], 'D': [1,0]}

maze = []
red_pos = []
blue_pos = []
hole_pos = []

def find_action(maze:list, red_pos:list):
    available = []
    if maze[red_pos[0]-1][red_pos[1]] == '.' or maze[red_pos[0]-1][red_pos[1]] ==  '0':
        available.append('U')
    if maze[red_pos[0]+1][red_pos[1]] == '.' or maze[red_pos[0]+1][red_pos[1]] ==  '0':
        available.append('D')
    if maze[red_pos[0]][red_pos[1]-1] == '.' or maze[red_pos[0]][red_pos[1]-1] == '0':
        available.append('L')
    if maze[red_pos[0]][red_pos[1]+1] == '.' or maze[red_pos[0]][red_pos[1]+1] == '0':
        available.append('R')
    return available

def do_action(maze:list, red_pos:list, blue_pos:list, hole_pos:list, count:int, action:str):
    if count > 10:
        return -1
 
    maze_copy = copy.deepcopy(maze)
    red_pos_copy = copy.deepcopy(red_pos)
    blue_pos_copy = copy.deepcopy(blue_pos)

    flag = False

    action_cmd = action_dict[action]
    while maze_copy[red_pos_copy[0] + action_cmd[0]][red_pos_copy[1] + action_cmd[1]] != '#'\
    and maze_copy[red_pos_copy[0] + action_cmd[0]][red_pos_copy[1] + action_cmd[1]] != 'B':
        red_pos_copy[0] += action_cmd[0]
        red_pos_copy[1] += action_cmd[1]
        if maze_copy[red_pos_copy[0]][red_pos_copy[1]] == '0':
            flag = True
            break

    maze_copy[red_pos[0]][red_pos[1]] = '.'
    maze_copy[red_pos_copy[0]][red_pos_copy[1]] = 'R'

    while maze_copy[blue_pos_copy[0] + action_cmd[0]][blue_pos_copy[1] + action_cmd[1]] != '#'\
    and maze_copy[blue_pos_copy[0] + action_cmd[0]][blue_pos_copy[1] + action_cmd[1]] != 'R':
        blue_pos_copy[0] += action_cmd[0]
        blue_pos_copy[1] += action_cmd[1]
        if maze_copy[blue_pos_copy[0]][blue_pos_copy[1]] == '0':
            return -1

    maze_copy[blue_pos[0]][blue_pos[1]] = '.'
    maze_copy[blue_pos_copy[0]][blue_pos_copy[1]] = 'B'

    if flag:
        return count

    available_actions = find_action(maze_copy, red_pos_copy)
    if available_actions == None:
        return -1

    min_res = 9999
    for available_action in available_actions:
        res = do_action(maze_copy, red_pos_copy, blue_pos_copy, hole_pos, count+1, available_action)
        if res != -1:
            min_res = min(min_res, res)
    if min_res == 9999:
        return -1
    else:
        return min_res

if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(n):
        row = input()
        cols = []
        for j in range(m):
            cols.insert(j, row[j])
            if row[j] == 'R':
                red_pos = [i, j]
            elif row[j] == 'B':
                blue_pos = [i, j]
            elif row[j] == '0':
                hole_pos = [i, j]
        maze.insert(i, cols)

    available_actions = find_action(maze, red_pos)
    min_count = 9999
    for available_action in available_actions:
        res = do_action(maze, red_pos, blue_pos, hole_pos, 1, available_action)
        if res != -1:
            min_count = min(min_count, res)
    
    if min_count == 9999:
        print(-1)
    else:
        print(min_count)
