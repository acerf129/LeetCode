class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        top,bot=0,rows-1
        mid=0
        while top<=bot:
            mid=(top+bot)//2
            if target>matrix[mid][-1]:
                top=mid+1
            elif target<matrix[mid][0]:
                bot=mid-1
            else:
                break
        #check the rows
        if not top<=bot:            
            return False
        mid=(top+bot)//2
        l,r=0,cols-1
        while l<=r:
            midcol =(l+r)//2
            if target>matrix[mid][midcol]:
                l=midcol+1
            elif target<matrix[mid][midcol]:
                r=midcol-1
            else:
                return True
        return False