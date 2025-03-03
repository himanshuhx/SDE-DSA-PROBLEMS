class Solution:
    def wordBreak(s, wordDict) -> bool:
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]