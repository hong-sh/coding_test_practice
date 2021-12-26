def get_fixed_point(n:int, nums:list):
    left, right = 0 , n-1

    while True:
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == mid:
            return mid

        if nums[mid] < mid:
            left = mid + 1

        if nums[mid] > mid:
            right = mid -1
        
if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(get_fixed_point(n, nums))