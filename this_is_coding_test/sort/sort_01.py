def reverse(numbers:list):
    numbers.sort(reverse=True)
    return numbers

if __name__ == "__main__":
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))

    print(reverse(numbers))