class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        f={}
        ans=0
        for num in nums:
            if not num in f:
                f[num]=0
            f[num]+=1
        
        for num in f:
            n=f[num]
            ans+=(n*(n-1)//2)
            
        return ans