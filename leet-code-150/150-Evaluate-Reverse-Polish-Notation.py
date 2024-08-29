class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        for x in tokens:
            try:
                int(x)
                stack.append(int(x))
            except ValueError:
                last = stack.pop()
                stack.append(ops[x](stack.pop(), last))
        return sum(stack)