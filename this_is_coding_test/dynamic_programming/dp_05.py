
def find_most_gold(n:int, m:int, dp:list):
    max_gold = -999
    for i in range(1, m):
        for j in range(n):
            current_gold = dp[j][i]
            left_up, left, left_down = 0, dp[j][i-1], 0
            if j - 1 >= 0:
                left_up = dp[j-1][i-1]
            if j + 1 < n:
                left_down = dp[j+1][i-1]

            dp[j][i] = current_gold + max([left, left_up, left_down])
            max_gold = max(max_gold, dp[j][i])

    return max_gold


if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        n, m = map(int, input().split())
        gold = list(map(int, input().split()))

        dp = []
        index = 0
        for i in range(n):
            dp.append(gold[index:index+m])
            index += m

        print(find_most_gold(n, m, dp))

    