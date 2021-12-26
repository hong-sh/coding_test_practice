def get_group_num(n:int, x_list:list):
    x_list.sort()
    current = 0
    start = 0
    group_cnt = 0
    while current < len(x_list):
        end = start + x_list[current]
        group = x_list[start : end]
        if group[-1] == len(group):
            group_cnt += 1
            start, current = end, end
            continue
        current += 1

    return group_cnt
if __name__ == "__main__":
    n = int(input())
    x_list = list(map(int, input().split()))
    print(get_group_num(n, x_list))