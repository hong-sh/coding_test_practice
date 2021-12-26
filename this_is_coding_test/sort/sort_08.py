def find_not_change(nums:list):
    idx_count = 0
    while True:
        max_num = nums[0]
        max_idx = 0
        for i in range(1, len(nums)-idx_count):
            if nums[i] > max_num:
                max_num = nums[i]
                max_idx = i
            
        if len(nums)-1-idx_count == max_idx:
            return nums[i]
        
        for i in range(max_idx, len(nums) - 1 - idx_count):
            nums[i] = nums[i+1]

        nums[len(nums)-1-idx_count] = max_num
        idx_count += 1

def find_not_change2(nums:list):
    nums_copy = copy.deepcopy(nums)
    nums_copy.sort(key= lambda x : x[0])

    max_idx = len(nums_copy) - 1
    while True:
        max_num = nums_copy[max_idx][0]
        for i in range(len(nums)):
            if max_num == nums[i][0] and max_idx != nums[i][1]:
                nums[i][1] = max_idx
            elif max_num == nums[i][0] and max_idx == nums[i][1]:
                return nums[i][0]

            else:
                if max_num < nums[i][0]:
                    nums[i][1] = nums[i][1] - 1 if nums[i][1] != 0 else 0
        max_idx -= 1

def find_not_change3(nums:list):
    sorted_nums = sorted(nums) 
    
    answer = 0 
    
    for i in range(len(sorted_nums)):
        answer = max(sorted_nums[i][1] - i + 1, answer)
    
    return answer

if __name__ == "__main__":
    n = int(input())
    nums = []
    for i in range(n):
        nums.append([int(input()), i])

    print(find_not_change3(nums))
    