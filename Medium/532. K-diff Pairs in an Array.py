class Solution:
    def findPairs(self, nums, k: int) -> int:
        result = []
        if k == 0:
            for i in nums:
                if nums.count(i) > 1 and (i,i) not in result:
                    result.append((i,i))
            return len(result)
        else:
            for i in nums:
                if nums.count(i-k) and (i-k,i) not in result:
                    result.append((i-k,i))
                # if nums.count(i+k) and (i,i+k) not in result:
                #     result.append((i,i+k))
            # print(result)
            return len(result)