class Solution:
    def tribonacci(self, n: int) -> int:
        one=1
        two=1
        three=0
        if n==0:
            return 0
        if n<=2:
            return 1
        for i in range(n-2):
            temp=one
            temp2=two
            one=one+two+three
            two=temp
            three=temp2
        return one