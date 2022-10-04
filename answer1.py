def isSubset(nums1:list[str], nums2:list[str]) -> bool:
    #if two subset sorted
    #if 2nd array is subset of 1st array
    #if both sorted O(log(n)) binary search

    n,m=len(nums1),len(nums2)    
    def binarySearch(i):
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if nums2[i]==nums1[mid]:
                return True
            if ord(nums1[mid])<ord(nums2[i]):
                l=mid+1
            else:
                r=mid-1          
               
        return False
    for i in range(m):
        if binarySearch(i):
            i+=1
        else:
            return False
    return True
    #or  
    n,m=len(nums1),len(nums2)    
    hashS=set()
    for i in range(n):
        hashS.add(nums1[i])
    for i in range(m):
        if nums2[i] not in hashS:
            return False
    return True
#time complexity O(m*log(n)) or O(m+n)
def test_isSubset():
    try:
        assert isSubset(["A","B","C","D","E"], ["A","E","D"])==True
    except AssertionError:
        print("case 1 error")
    try:
        assert isSubset(["A","B","C","D","E"], ["A","D","Z"])==False
    except AssertionError:
        print("case 2 error")
    try:
        assert isSubset(["A","D","E"],["A","A","D","E"])==True
    except AssertionError:
        print("case 3 error")
    try:
        assert isSubset(["A","D","E","Z"],["A","A","D","E"])==True
    except AssertionError:
        print("case 3 error")
def main():
    test_isSubset()
if __name__=="__main__":
    main()