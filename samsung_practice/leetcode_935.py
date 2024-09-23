class Solution:
    def knightDialer(self, n: int) -> int:
        move_dict = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        
        dp = {}
        
        def dfs(dial, n):
            if n == 1:
                dp[(dial, n)] = 1
                return dp[(dial, n)]
            
            if (dial, n) in dp:
                return dp[(dial, n)]
            
            count = 0
            for move in move_dict[dial]:
                count += dfs(move, n-1)
            
            dp[(dial, n)] = count
            return count
        
        sum_count = 0
        for i in range(10):
            sum_count += dfs(i, n)
            
        return sum_count % (10**9 + 7)
    
sol = Solution()
print(sol.knightDialer(3131))