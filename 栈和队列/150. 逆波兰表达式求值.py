# https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/submissions/
class Solution:
    def calculate(self, num1, num2, operateor):
        if operateor == '+':
            return num1 + num2
        if operateor == '-':
            return num1 - num2
        if operateor == '*':
            return num1 * num2
        if operateor == '/':
            return num1 / num2

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if stack and token in ('+', '-', '*', '/'):
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(self.calculate(num1, num2, token))
            else:
                stack.append(token)
        return int(stack[-1])
