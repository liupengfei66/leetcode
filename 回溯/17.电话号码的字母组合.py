# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []
        phone = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
        '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def backTracking(digits, k):
            if len(digits) == k:
                res.append("".join(path[:]))
                return res
            # 对输入不在2-9的处理
            if digits[k] not in phone:
                raise ValueError("input is invalid!")
            for char in phone[digits[k]]:
                path.append(char)
                backTracking(digits, k+1)
                path.pop()

        if len(digits) == 0:
            return res
        backTracking(digits, 0)
        return res
