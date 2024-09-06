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
            elif c in \-+\:
                res += num*sign
                sign = -1 if c is \-\ else 1
                num = 0
            elif c is \(\:
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c is \)\:
                res += num*sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign