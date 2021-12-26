coin = [0] * 10001

def get_coin(mm:int):
    mid = mm // 2
    min_cnt = 9999999
    for i in range(mid+1):
        if coin[i] == 0 or coin[mm-i] == 0:
            continue
        
        min_cnt = min(min_cnt, coin[i] + coin[mm-i])
    coin[mm] = min_cnt if min_cnt != 9999999 else 0

def get_safiesfy(m:int):
    for i in range(m+1):
        if coin[i] == 1:
            continue
        get_coin(i)

    return coin[m] if coin[m] != 0 else -1

if __name__ == "__main__":
    n , m = map(int, input().split())
    for _ in range(n):
        coin[int(input())] = 1

    print(get_safiesfy(m))