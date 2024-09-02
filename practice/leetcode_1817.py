from typing import List

from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0] * k
        user_dict = defaultdict(set)
        for id_, time in logs:
            user_dict[id_].add(time)
            
        for id_ in user_dict:
            answer[len(user_dict[id_]) - 1] += 1
            
        return answer
    
if __name__ == "__main__":
    logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
    k = 5
    print(Solution().findingUsersActiveMinutes(logs, k))
    