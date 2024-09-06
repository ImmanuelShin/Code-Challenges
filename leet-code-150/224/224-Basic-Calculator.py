class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        res = 0
        stack = []

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            elif c in "-+":
                res += num*sign
                sign = -1 if c is "-" else 1
                num = 0
            elif c is "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c is ")":
                res += num*sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign

class FailedSolution:
    def calculate(self, s: str) -> int:
        stack = []
        paren = []
        digit = True
        for i, c in enumerate(s):
            stack.append(c)
            if c == "(":
                paren.append(i)
            if c == ")":
                index = paren.pop()
                num = self.evaluate(stack[index:])
                stack[index:] = []
                stack.append(num)
            if c == "+" or c == "-":
                digit = False
        if digit:
            return int(re.sub(r"\D", "", s))
        return self.evaluate(stack)
            
    def evaluate(self, s):
        cur = 0
        prev = "+"
        for c in s:
            if str(c).isnumeric() or (str(c).startswith("-") and str(c)[1:].isnumeric()):
                match prev:
                    case "+":
                        cur = cur + int(c)
                    case "-":
                        cur = cur - int(c)
            elif c == "+" or c == "-":
                prev = c
        return cur