class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #hashmap 23 2 4 6 7  
        #remain index
        #5 0
        #1 1
        #5 2 
        #0 -1
        #0 0
        check={0:-1}
        sums=0
        for i,n in enumerate(nums):        
            sums+=n
            remain=sums%k                        
            if remain in check :
                if i-check[remain]>=2:
                    return True
            else:
                check[remain]=i
        return False