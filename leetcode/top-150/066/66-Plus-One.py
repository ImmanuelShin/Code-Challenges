class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1 and digits[0] == 9:
            digits = [1, 0]
        elif digits[-1] == 9:
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] == 9 and i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                    break
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
        else:
            digits[-1] += 1
        return digits