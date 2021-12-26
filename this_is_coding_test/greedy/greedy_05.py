def make_biggist_num(numbers:list):
    res = 0
    for number in numbers:
        number = int(number)
        if number == 0 or number == 1 or res == 0 or res == 1:
            res += number
        else:
            res *= number
    return res

if __name__ == "__main__":
    numbers = list(input())
    print(make_biggist_num(numbers))