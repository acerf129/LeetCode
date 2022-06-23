class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #123456
        #3. 6. 2.  5. 4. 1  
        nums.sort()
        l,r=0,len(nums)-1
        mid= (len(nums)-1) //2
        temp=sorted(nums)
        mid2=mid
        for i in range(len(nums)):
            if not i%2:
                nums[i]=temp[mid2]
                mid2-=1
            else:
                nums[i]=temp[r]
                r-=1
        