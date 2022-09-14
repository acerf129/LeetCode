class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        l,r=1,num
        
        while l<=r:
            mid=(l+r)//2
            if mid**2==num:
                return True
            if mid**2<num and (mid+1)**2>num:
                return False
            if mid**2<num:
                l=mid+1
            else:
                r=mid-1
            
        return False