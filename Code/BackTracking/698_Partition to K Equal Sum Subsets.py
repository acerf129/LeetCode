class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sums=sum(nums)
        if sums%k:
            return False
        target=sums//k
        used=[False]*len(nums)
        dic={}
        def backtrack(cur,k,ith):
            if k==0:
                return True
            if cur>target:
                return False
            if (cur,ith) in dic:
                return dic[(cur,ith)]
            if cur==target:
                dic[(cur,ith)]=backtrack(0,k-1,ith)
                return dic[(cur,ith)]
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    temp=ith
                    ith=ith |1<<i
                    if backtrack(cur+nums[i],k,ith):
                        dic[(cur,ith)]=True
                        return True
                    ith=temp
                    used[i]=False
            dic[(cur,ith)]=False
            return False
        return backtrack(0,k,0)