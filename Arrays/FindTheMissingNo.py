# if sorting is allowed
def find(arr):
    arr.sort()
    for i,num in enumerate(arr):
        if i+1 != num:
            return i+1

#using formula of first n number
def find(arr):
    n = len(arr)+1 #1 extra because arr len is n + 1 missing no
    arr_sum = sum(input())
    expected_output = (n*(n+1))/2
    return expected_output-arr_sum

#using sum=1 and counter =2 approach
def find(arr):
    sum=1
    counter = 2
    for num in arr:
        sum = sum - num + counter
        counter += 1
    return sum

#using Xor approach 1^2^3^4^5= X and 1^2^3^5 = Y, X^Y = 4
def find(arr):
    x = arr[0]
    y = 1
    for i in range(1,len(arr)):
        x = x^arr[i]
    for i in range(2,n+2):
        y = y^i
    return x^y

