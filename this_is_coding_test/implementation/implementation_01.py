command_map = [(0,-1), (0,1), (-1,0), (1,0)] # L R U D

def get_position(size:int, commands:list):
    start_pos = (1, 1)
    for command in commands:
        if command == 'L':
            next_pos = (start_pos[0] + command_map[0][0], start_pos[1] + command_map[0][1])
            if next_pos[1] >= 1:
                start_pos = next_pos
        elif command == 'R':
            next_pos = (start_pos[0] + command_map[1][0], start_pos[1] + command_map[1][1])
            if next_pos[1] <= size:
                start_pos = next_pos
        elif command == 'U':
            next_pos = (start_pos[0] + command_map[2][0], start_pos[1] + command_map[2][1])
            if next_pos[0] >= 1:
                start_pos = next_pos
        elif command == 'D':
            next_pos = (start_pos[0] + command_map[3][0], start_pos[1] + command_map[3][1])
            if next_pos[0] <= size:
                start_pos = next_pos

    return start_pos

if __name__ == "__main__":
    size = int(input())
    commands = list(map(str, input().split()))
    print(get_position(size, commands))