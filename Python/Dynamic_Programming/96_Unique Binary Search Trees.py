class Solution:
    def numTrees(self, n: int) -> int:
        # numT 4 = num[0]*3+
        #          num[1]*2+
        numT=[1]*(n+1)
        for i in range(2,n+1):
            #if 2  1 2
            total=0
            for root in range(1,i+1):
                #if 2 in 4 left=1 right=2
                left=root-1
                right=i-root
                total+=numT[left]*numT[right]
            numT[i]=total
        return numT[n]