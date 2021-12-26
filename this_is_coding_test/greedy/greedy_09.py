def get_food(food_times:list, k:int):
    food_tuple = []
    for i in range(len(food_times)):
        food_tuple.append([food_times[i], i+1])
    
    food_tuple.sort(key=lambda x : x[0])
    
    while len(food_tuple) > 0:
        after = len(food_tuple) * food_tuple[0][0]
        if after >= k:
            food_tuple.sort(key = lambda x : x[1])
            return food_tuple[k % len(food_tuple)][1]
        
        k -= after
        for i in range(len(food_tuple)):
            food_tuple[i][0] -= 1 * after // len(food_tuple)
        del food_tuple[0]

    return -1

if __name__ == "__main__":
    food_times = list(map(int, input().split()))
    k = int(input())
    print(get_food(food_times, k))

