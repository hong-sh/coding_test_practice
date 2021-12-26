def get_biggest(n:int, m:int, cards:list):
    max_num = 0
    for i in range(n):
        if(max_num < min(cards[i])):
            max_num = min(cards[i])
    return max_num


if __name__ == "__main__":
    n, m = map(int, input().split())
    cards = []
    for i in range(n):
        numbers = list(map(int, input().split()))
        cards.insert(i, numbers)
    print(get_biggest(n, m, cards))