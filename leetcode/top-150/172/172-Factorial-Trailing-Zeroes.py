sys.set_int_max_str_digits(0)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        fac = math.factorial(n)
        fac = str(fac)
        return len(fac) - len(fac.rstrip('0'))