def get_target(n:int, data:list):
    target = 1
    for x in data:
        if target < x:
            break
        target += x
    return target

if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    print(get_target(n, data))