def make_one(n, k):
    pow_num = k
    pow_cnt = 0
    while n >= pow_num:
        pow_num *= k
        pow_cnt += 1
    return pow_cnt + n - pow(k, pow_cnt)


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(make_one(n, k))