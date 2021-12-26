
def exist_nums(nums:list, finds:list):
    nums.sort()

    exist = []
    for find in finds:
        left , right = 0, len(nums)-1
        while True:
            if left > right:
                exist.append(0)
                break

            mid = (left + right) // 2
            if nums[mid] == find:
                exist.append(1)
                break
            
            if nums[mid] < find:
                left = mid + 1

            if nums[mid] > find:
                right = mid - 1
            
    return exist

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    m = int(input())
    finds = list(map(int, input().split()))

    rsts = exist_nums(nums, finds)
    for rst in rsts:
        print(rst)