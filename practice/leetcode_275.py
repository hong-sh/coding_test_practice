from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        len_citations = len(citations)
        
        left, right = 0, len_citations-1
        
        while left <= right:
            mid = (left + right) // 2
            citation = citations[mid]
            if citation == (len_citations - mid):
                return citation
            
            if citation < (len_citations - mid):
                left = mid + 1
            
            else:
                right = mid - 1
                
        return len_citations - left
    