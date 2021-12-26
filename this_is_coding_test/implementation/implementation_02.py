def get_three_count(time:int):
    three_count = (1575, 3600)
    if time < 3:
        return (time + 1) * three_count[0]
    elif time >= 3 and time < 13:
        return time * three_count[0] + three_count[1]
    elif time >= 13 and time < 23:
        return (time - 1) * three_count[0]  + 2 * three_count[1]
    elif time >= 23:
        return (time - 2) * three_count[0] + 3 * three_count[1]

if __name__ == "__main__":
    time = int(input())
    print(get_three_count(time))