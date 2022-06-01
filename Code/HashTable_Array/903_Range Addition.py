class Solution:
    def get_modified_array(self, length: int, updates: List[List[int]]) -> List[int]:
        # Write your code here
        nums=[0]*(length)
        #from 1 to 3 +2
        #0 0 0 0 0 
        #0 2 0 0 -2 
        #0 5 0 0 0 
        for l in updates:
            start=l[0]
            end=l[1]
            increment=l[2]
            nums[start]+=increment
            if end+1<length:
                nums[end+1]-=increment
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums