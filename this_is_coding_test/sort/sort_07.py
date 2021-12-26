from queue import PriorityQueue

def get_minimum_compare(card_nums:PriorityQueue):
    sum_compare = 0
    while card_nums.qsize() > 1:
        num1 = card_nums.get()
        num2 = card_nums.get()
        compare = num1 + num2
        sum_compare += compare
        card_nums.put(compare)
        
    return sum_compare

if __name__ == "__main__":
    n = int(input())
    card_nums = PriorityQueue()
    for _ in range(n):
        card_nums.put(int(input()))

    print(get_minimum_compare(card_nums))
    