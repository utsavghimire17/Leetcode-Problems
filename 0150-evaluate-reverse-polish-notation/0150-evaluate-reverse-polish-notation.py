class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        int_tokens = []
        stack = []
        operators = {"/","+","-","*"}
        for val in tokens:
            if val not in operators:
                int_tokens.append(int(val))
            else:
                int_tokens.append(val)
        for token in int_tokens:
            if token in operators and len(stack) >= 2:
                val = stack.pop()
                if token == "+":
                    stack[-1] = stack[-1] + val
                elif token == "-":
                    stack[-1] = stack[-1] - val
                elif token == "*":
                    stack[-1] = stack[-1] * val
                elif token == "/":
                    stack[-1] = int(stack[-1] / val)
            else:
                stack.append(token)
        return stack[-1]