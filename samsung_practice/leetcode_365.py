class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # 1. fill x, 2. fill y, 3. empty x, 4. empty y, 5. x -> y, 6. x <- y
        
        seen = set()
        
        def dfs(total):
            if total == target:
                return True
            
            if total in seen or total < 0 or total > x + y:
                return False

            seen.add(total)
            
            return dfs(total + x) or dfs(total - x) or dfs(total + y) or dfs(total - y)
            
        return dfs(0)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canMeasureWater(3, 5, 4))
    
    