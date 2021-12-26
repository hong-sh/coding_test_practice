
def get_combination(n:int, m:int, weights:list):
    weights_cnt = [0] * m
    for weight in weights:
        weights_cnt[weight-1] += 1

    combination = n * (n-1) // 2

    for weight_cnt in weights_cnt:
        combination -= weight_cnt * (weight_cnt-1) // 2

    return combination

if __name__ == "__main__":
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    print(get_combination(n, m, weights))