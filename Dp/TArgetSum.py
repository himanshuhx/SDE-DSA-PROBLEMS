def tSum(arr,n,sum):
    if sum==0:
        return True
    if n==0:
        return False
    if arr[n-1]>sum:
        return False
    return tSum(arr,n-1,sum) or tSum(arr,n-1,sum-arr[n-1])

def tSum(arr,n,sum):
    dp = [[False for i in range(sum+1)] for j in range(n+1)]
    for i in range(sum+1):
            dp[0][i]=False
    for j in range(n+1):
            dp[j][0]=True
    for i in range(1,sum+1):
        for j in range(1,n+1):
            if dp[i][j]>sum:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i][j-arr[i-1]]
    return dp[-1][-1]