def solve(arr, n, k):
    if n == 0:
        return 0
    x = solve(arr, n-1, k)
    y = (x + k) % n
    return y

