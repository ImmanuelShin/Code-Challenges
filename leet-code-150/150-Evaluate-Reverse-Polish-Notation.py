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
            if x in ops:
                last = stack.pop()
                stack.append(ops[x](stack.pop(), last))
            else:
                int(x)
                stack.append(int(x))
        return sum(stack)