
def get_length(n:int, m:int, rices:list):
    min_length = 1
    max_length = max(rices)

    while True:
        mid = (min_length + max_length) // 2

        remain_length = 0
        for rice in rices:
            remain_length = remain_length + (rice - mid) if (rice - mid) > 0 else remain_length

        if remain_length == m:
            return mid

        if remain_length < m:
            max_length = mid - 1
        
        elif remain_length > m:
            min_length = mid + 1

        if min_length >= max_length:
            return mid


if __name__ == "__main__":
    n, m = map(int, input().split())
    rices = list(map(int, input().split()))
    print(get_length(n, m, rices))
