dp = [99999] * 30001

if __name__ == "__main__":
    dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 1

    n = int(input())
    for i in range(6, n+1):
        dp[i] = dp[i-1] + 1

        if dp[i] % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if dp[i] % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if dp[i] % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)

    print(dp[n])