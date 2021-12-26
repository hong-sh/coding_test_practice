import itertools

def get_zero_set(acids:list):
    combinations = list(itertools.combinations(acids, 2))
    diff_min = 9999
    diff_set = None
    for combination in combinations:
        combination_diff = abs(combination[0] + combination[1])
        if diff_min > combination_diff:
            diff_set = (combination[0], combination[1])
            diff_min = combination_diff

    return diff_set

def get_zero_set2(acids:list):
    left = 0
    right = len(acids) -1
    min_diff = 999999999999999
    min_set = None
    while left < right:
        diff = acids[left] + acids[right]

        abs_diff = abs(diff)
        if abs_diff < min_diff:
            min_set = (acids[left], acids[right])
            min_diff = abs_diff

        if diff < 0:
            left += 1
        if diff > 0 :
            right -= 1
        if diff == 0:
            return (acids[left], acids[right])

    return min_set

if __name__ == "__main__":
    n = int(input())
    acids = list(map(int, input().split()))
    rst = get_zero_set2(acids)
    print(rst[0], rst[1])