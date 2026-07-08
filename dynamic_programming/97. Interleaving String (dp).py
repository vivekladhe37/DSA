class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if len(s3) != m + n:
            return False

        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and dp[i-1][j] and s3[i + j - 1] == s1[i - 1]:
                    dp[i][j] = True
                if j > 0 and dp[i][j-1] and s3[i + j - 1] == s2[j - 1]:
                    dp[i][j] = True

        return dp[m][n]




        