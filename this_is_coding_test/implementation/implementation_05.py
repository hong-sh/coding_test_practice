def get_available(score:str):
    first = 0
    second = 0
    for i in range(len(score)):
        if i < len(score) // 2:
            first += int(score[i])
        else:
            second += int(score[i])

    if first == second:
        return 'LUCKY'
    else:
        return 'READY'


if __name__ == "__main__":
    score = input()
    print(get_available(score))