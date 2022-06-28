class Solution:
    def minDeletions(self, s: str) -> int:
        count=Counter(s)
        req=0
        check=set()
        print(sorted(count.values()))
        for i  in sorted(count.values()):
            val=i
            while val  in check :
                val-=1
                req+=1
                if val==0 and val in check:
                    break
            else:
                check.add(val)
        return req