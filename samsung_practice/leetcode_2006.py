from typing import List

from itertools import combinations

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        answer = 0
        
        len_num = len(nums)
        for i in range(len_num):
            for j in range(i+1, len_num):
                if abs(nums[i]-nums[j]) == k:
                    answer += 1
                
        return answer
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countKDifference([1, 2, 2, 1], 1))