# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 16:15

class Solution:
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
            else:
                if left < n:
                    S.append('(')
                    backtrack(S, left+1, right)
                    S.pop()
                if right < left:
                    S.append(')')
                    backtrack(S, left, right+1)
                    S.pop()

        backtrack([], 0, 0)
        return ans

a = Solution()
print(a.generateParenthesis(2))