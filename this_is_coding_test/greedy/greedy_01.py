
def get_sum(n:int, m:int, k:int, numbers:list):
    numbers.sort(reverse=True)
    first = numbers[0]
    second = numbers[1]

    div = m // (k+1)
    mod = m % (k+1)

    return (first * k + second) * div + first * mod


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(get_sum(n, m, k, numbers))
