class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        req=0
        maxl,maxr=height[l],height[r]
        while l<r:
            if maxl<maxr:
                l+=1
                maxl=max(maxl,height[l])
                #if there is any left higher than curr add the deficit
                req+=maxl-height[l]
            else:
                r-=1
                maxr=max(maxr,height[r])
                req+=maxr-height[r]
        return req