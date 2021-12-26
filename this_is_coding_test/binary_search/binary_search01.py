def bs(find:int, parts:list, left:int, right:int):
    mid = (left + right) // 2
    if parts[mid] == find:
        return 'yes'

    if left >= right:
        return 'no'

    if parts[mid] < find:
        return bs(find, parts, mid+1, right)
    elif parts[mid] > find:
        return bs(find, parts, 0, left-1)


def find_parts(n:int, m:int, parts:list, finds:list):
    rsts = []
    parts.sort()
    for find in finds:
        rsts.append(bs(find, parts, 0, len(parts)))

    return rsts


if __name__ == "__main__":
    n = int(input())
    parts = list(map(int, input().split()))

    m = int(input())
    finds = list(map(int, input().split()))

    rsts = find_parts(n, m, parts, finds)
    for rst in rsts:
        print(rst, end=' ')

