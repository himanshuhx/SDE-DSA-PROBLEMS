'''
 intusion - if n is odd n-- and update ans to ans*x
 also an integer can overflow if n is -ve so consider long long
 we are keeping m in plce of n to keep track of n whether it is +ve or -ve
 to use in last step
'''



class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = -1*n if n<0 else n
        ans = 1
        while m:
            if m%2:
                ans = ans*x
                m -= 1
            else:
                x *= x
                m = m//2
        return ans if n>=0 else 1/ans