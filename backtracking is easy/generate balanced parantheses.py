# rule 1 can place left parenthese until its >0
# rule 2 can place right parentheses until left<right
# this is because a valid string will always start from '('

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(n, left, right, s):
            nonlocal ans
            if right < left:
                return
            if left == right == 0:
                ans.append(s)
                return
            if left:
                dfs(n, left - 1, right, s + '(')
            if right:
                dfs(n, left, right - 1, s + ')')

        ans = []
        dfs(n, n, n, "")
        return ans