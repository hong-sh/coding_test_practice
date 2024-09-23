from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        dp_max = [0] * len_prices
        dp_min = [0] * len_prices
        dp_min[0] = prices[0]
        
        for i in range(1, len_prices):
            if (prices[i] - dp_min[i-1]) > dp_max[i-1]:
                dp_max[i] = prices[i] - dp_min[i-1]
            else:
                dp_max[i] = dp_max[i-1]
            
            if dp_min[i-1] > prices[i]:
                dp_min[i] = prices[i]
            else:
                dp_min[i] = dp_min[i-1]
                
        return dp_max[-1]
    
    
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))