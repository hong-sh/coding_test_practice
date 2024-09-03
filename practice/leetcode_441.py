class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        stair = 0
        while True:
            if n < stair+1:
                return stair
            
            stair += 1
            n -= stair
            

sol = Solution()
print(sol.arrangeCoins(5))