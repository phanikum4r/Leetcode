class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        operator = '+'
        i = 1
        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            if ch in '+-*/' or i == len(s):
                if operator == '+':
                    stack.append(operand)
                    operator = ch
                elif operator == '-':
                    stack.append(-operand)
                    operator = ch
                elif operator == '*':
                    stack.append(stack.pop() * operand)
                    operator = ch
                elif operator == '/':
                    stack.append(int(stack.pop() / operand))
                    operator = ch
                operand = 0
            i += 1
        return sum(stack)