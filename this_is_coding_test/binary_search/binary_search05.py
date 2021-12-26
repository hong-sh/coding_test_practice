import itertools 
def get_pos(n:int, c:int, houses:list):
    houses.sort()
    combination_list = list(itertools.combinations(houses, c))

    min_max = 0
    for combination in combination_list:
        min_diff = 99999
        for i in range(len(combination)-1):
            min_diff = min(min_diff, abs(combination[i] - combination[i+1]))
        min_max = max(min_max, min_diff)

    return min_max

if __name__ == "__main__":
    n, c = map(int, input().split())
    houses = []
    for _ in range(n):
        houses.append(int(input()))

    print(get_pos(n, c, houses))
