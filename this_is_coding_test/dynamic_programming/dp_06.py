def get_count(numbers:list):
    max_count = 0
    dp = [0] * (len(numbers) + 1)

    for i in range(len(numbers)):
        dp[numbers[i]] = i

    for i in range(1, len(dp)):
        count = [1]
        count_idx = 0
        sub_min = dp[i]

        for j in range(i+1, len(dp)):
            if sub_min < dp[j] and dp[i] < dp[j]:
                count[count_idx] += 1
                sub_min = dp[j]

            elif sub_min > dp[j] and dp[i] < dp[j]:
                count.append(2)
                count_idx += 1
                sub_min = dp[j]

        max_count = max(max_count, max(count))
        
    return len(numbers) - max_count


if __name__ == "__main__":
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))

    print(get_count(numbers))