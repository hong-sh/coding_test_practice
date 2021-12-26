def get_fail_rate(fail_list:list, stages:list):
    for stage in stages:
        fail_list[(stage-1)] += 1

    fail_rate = []
    for i in range(len(fail_list)-1):
        user_num = sum(fail_list[i:])
        
        fail_rate.append((i+1, fail_list[i] / user_num))

    fail_rate.sort(key= lambda x : x[1], reverse=True)
    return fail_list

if __name__ == "__main__":
    n = int(input())
    fail_list = [0] * (n+1)
    stages = list(map(int, input().split()))
    fail_list = get_fail_rate(fail_list, stages)
    for fail in fail_list:
        print(fail[0], end=', ')
