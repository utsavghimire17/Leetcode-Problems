class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        int_tokens = []
        stack = []
        operations = {'/': lambda a,b: int(a/b),
                    '+': lambda a,b: a + b,
                    "*": lambda a,b: a * b,
                    "-": lambda a,b: a - b}
        for val in tokens:
            if val not in operations:
                int_tokens.append(int(val))
            else:
                int_tokens.append(val)
        for token in int_tokens:
            if token in operations and len(stack) >= 2:
                val = stack.pop()
                operation = operations[token]
                stack[-1] = operation(stack[-1], val)
            else:
                stack.append(token)
        return stack[-1]