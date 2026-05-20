class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(s,t,i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j] !=-1:
                return dp[i][j]
            if s[i]==t[j]:
                dp[i][j]= 1 + helper(s,t,i-1,j-1)
                return dp[i][j]
            dp[i][j]= max(helper(s,t,i-1,j),helper(s,t,i,j-1))
            return dp[i][j]
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return helper(text1,text2,len(text1)-1,len(text2)-1)

        
