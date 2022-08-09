class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.tree=[0]*4*len(nums)
        def buildtree(node,start,end):
            if start==end:
                self.tree[node]=self.nums[start]
                return 
            mid=(start+end)//2
            leftnode=2*node+1
            rightnode=2*node+2
            buildtree(leftnode,start,mid)
            buildtree(rightnode,mid+1,end)
            self.tree[node]=self.tree[leftnode]+self.tree[rightnode]
        buildtree(0,0,len(self.nums)-1)
    def update(self, index: int, val: int) -> None:
        def updatree(node,start,end):
            if start==end:
                #update from bottom
                self.tree[node]=self.nums[index]=val
                return 
            mid=(start+end)//2
            leftnode=2*node+1
            rightnode=2*node+2
            if start<=index<=mid:
                updatree(leftnode,start,mid)
            else:
                updatree(rightnode,mid+1,end)
            self.tree[node]=self.tree[leftnode]+self.tree[rightnode]
        updatree(0,0,len(self.nums)-1)

    def sumRange(self, left: int, right: int) -> int:
        def query(node,start,end):
            if end<left or start>right:
                return 0
            if left<=start<=end<=right:
                return self.tree[node]
            mid=(start+end)//2
            leftnode=2*node+1
            rightnode=2*node+2
            leftsum=query(leftnode,start,mid)
            rightsum=query(rightnode,mid+1,end)
            return leftsum+rightsum
        return query(0,0,len(self.nums)-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)