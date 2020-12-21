def reverse(arr,n,k):
    i=0
    while i<n:
        left = i
        right = min(i+k-1,n-1)
        while left<right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        i+=k
    return arr
# 0n time 01 space