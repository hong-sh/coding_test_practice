a_to_i = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
def get_case(night_pos:str):
    position = (a_to_i[night_pos[0]], int(night_pos[1]))
    move_cases = [(-2, 1), (-1, 2), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
    count = 0
    for move_case in move_cases:
        x = position[0] + move_case[0]
        y = position[1] + move_case[1]
        if x >= 1 and x <= 8 and y >= 1 and y <= 8:
            count += 1

    return count

if __name__ == "__main__":
    night_pos = input()
    print(get_case(night_pos))