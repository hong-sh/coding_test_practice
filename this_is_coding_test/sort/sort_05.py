from itertools import permutations
from collections import defaultdict
def get_cost(pairs:list):
    cost_dict = defaultdict(int)
    for pair in pairs:
        cost_dict[pair[0]] += abs(pair[0] - pair[1])
    cost_list = sorted(cost_dict.items(), key= lambda x : (x[1], x[0]))
    return cost_list[0][0]

if __name__ == "__main__":
    n = int(input())
    houses = list(map(int, input().split()))
    houses.sort()
    # pairs = list(permutations(houses, 2))
    # print(get_cost(pairs))
    print(houses[n//2 - 1])
