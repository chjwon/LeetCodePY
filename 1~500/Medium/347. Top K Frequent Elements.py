from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        from heapq import heappop, heappush
        sol = []
        solDic = Counter(nums)
        for key, val in solDic.items():
            heappush(sol,(val,key))
            if len(sol) > k:
                heappop(sol)
        for temp in range(len(sol)):
            sol[temp] = sol[temp][1]
        return sol