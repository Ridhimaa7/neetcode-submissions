class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["*","/","+","-"]
        stack = []
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
                continue
            a = stack.pop()
            b = stack.pop()
            if token == '+':
                res = a + b
            elif token == '-':
                res = b - a
            elif token == "*":
                res = a * b
            elif token == "/":
                res = int(b / a)
            stack.append(res)
        return stack[0]