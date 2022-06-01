class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        req=0
        while l<r:
            while height[l]<height[r]:
                req=max(req,min(height[l],height[r])*(r-l))
                l+=1
            req=max(req,min(height[l],height[r])*(r-l))
            r-=1
        return req
        l,r=0,len(height)-1
        req=0
        while l<r:
            req=max(req,min(height[l],height[r])*(r-l))
            if  height[l]<height[r]:
                l+=1
            else:
                r-=1
        return req