def get_count(numbers:list):
    cnts = [0,0]

    buffer = 0
    for number in numbers:
        number = int(number)
        if number == 0:
            if buffer != number:
                cnts[1] += 1
            buffer = number
        else:
            if buffer != number:
                cnts[0] += 1
            buffer = number
    cnts[buffer] += 1
    return min(cnts[0], cnts[1])

if __name__ == "__main__":
    # 11110011
    numbers = list(input())
    print(get_count(numbers))