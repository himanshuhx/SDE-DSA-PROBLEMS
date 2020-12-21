def dp(arr):
    lis = [1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if lis[i]>lis[j]:
                lis[i] = max(lis[i],lis[j]+1)
    ans = 1
    ans = max(lis)
    return ans