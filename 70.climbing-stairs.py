class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        a=[0]*n
        a[1]=1
        a[2]=2
        def climb(n):
            if a[n]!=0:
                return a[n]
            else:
                a[n]=climb(n-1)+climb(n-2)
                return a[n]

        return climb(n-1)+climb(n-2)
        
