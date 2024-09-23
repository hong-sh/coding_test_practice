from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        len_piles = len(piles)
        
        #dp = [[[-1 for _ in range(2)] for _ in range(len_piles)] for _ in range(len_piles)] # idx, M, turn
        dp = {}
        
        def dfs(start_idx, M, turn, len_piles):
            if start_idx == len_piles:
                return 0
            
            if (start_idx, M, turn) in dp:
            #if dp[start_idx][M][turn] != -1:
                return dp[(start_idx, M, turn)]
            
            
            score = 0 if turn else float('inf')
            total = 0
            
            for X in range(1, 2*M+1):
                if start_idx + X > len_piles:
                    break
                
                total += piles[start_idx+X-1]
                
                if turn: # alice
                    score = max(score, total + dfs(start_idx+X, max(M, X), 0, len_piles))

                else:
                    score = min(score, dfs(start_idx+X, max(M, X), 1, len_piles))
            
            dp[(start_idx, M, turn)] = score
            return score
        
        return dfs(0, 1, 1, len_piles)
        
sol = Solution()
print(sol.stoneGameII(piles=[1]))